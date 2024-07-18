from flask import Blueprint, request, jsonify
import requests
import os


api_key = os.getenv('WEATHER_API_KEY')
weather = Blueprint('weather', __name__)


@weather.route('/current', methods=['GET'])
def get_current_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = request.args.get('city')
    
    if not city_name:
        return jsonify({'error': 'City name is required'}), 400
    
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        return jsonify({
            'temperature': temperature,
            'pressure': pressure,
            'humidity': humidity,
            'description': weather_description
        })
    else:
        return jsonify({'error': 'City Not Found'}), 404
    
@weather.route('/forecast', methods=['GET'])
def get_weather_forecast():
    city_name = request.args.get('city')
    
    if not city_name:
        return jsonify({'error': 'City name is required'}), 400
    
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == "200":
        forecast_list = data["list"]
        return jsonify({'forecast': forecast_list})
    else:
        return jsonify({'error': 'City Not Found'}), 404

@weather.route('/air_pollution', methods=['GET'])
def get_air_pollution():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not lat or not lon:
        return jsonify({'error': 'Latitude and longitude are required'}), 400
    
    base_url = "http://api.openweathermap.org/data/2.5/air_pollution?"
    complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    
    if "list" in data:
        return jsonify({'air_pollution': data['list']})
    else:
        return jsonify({'error': 'Data not found'}), 404
    