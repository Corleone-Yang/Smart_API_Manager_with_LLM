from flask import Blueprint, render_template, jsonify, request
from .classification import classify_prompt


routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/result', methods=['POST'])
def result():
    user_input = request.form['userInput']
    res = classify_prompt(user_input)
    
    if res == "[0, 0]":
        route = "/calculator/add"
    elif res == "[0, 1]":
        route = "/calculator/subtract"
    elif res == "[0, 2]":
        route = "/calculator/multiply"
    elif res == "[0, 3]":
        route = "/calculator/divide"
    elif res == "[0, 4]":
        route = "/calculator/power"
    elif res == "[0, 5]":
        route = "/calculator/sqrt"
    elif res == "[0, 6]":
        route = "/calculator/log"
    elif res == "[0, 7]":
        route = "/calculator/factorial"
    elif res == "[0, 8]":
        route = "/calculator/sin"
    elif res == "[0, 9]":
        route = "/calculator/cos"
    elif res == "[0, 10]":
        route = "/calculator/tan"
    elif res == "[1, 0]":
        route = "/notes/create"
    elif res == "[1, 1]":
        route = "/notes/display"
    elif res == "[1, 2]":
        route = "/notes/<int:note_id>"
    elif res == "[1, 3]":
        route = "/notes/delete/<int:note_id>"
    elif res == "[1, 4]":
        route = "/notes/update/<int:note_id>"
    elif res == "[2, 0]":
        route = "/weather/current"
    elif res == "[2, 1]":
        route = "/weather/forecast"
    elif res == "[2, 2]":
        route = "/weather/air_pollution"
    elif res == "[3, 0]":
        route = "/translate"
    elif res == "[4, 0]":
        route = "/email/compose_email"
    elif res == "[4, 1]":
        route = "/email/send_email"
    elif res == "[4, 2]":
        route = "/email/read_email"
    elif res == "[4, 3]":
        route = "/email/delete_email"
    elif res == "[5, 0]":
        route = "/notification/send_notification"
    elif res == "[5, 1]":
        route = "/notification/view_notifications"
    elif res == "[5, 2]":
        route = "/notification/mark_as_read"
    elif res == "[5, 3]":
        route = "/notification/delete_notification"
    elif res == "[6, 0]":
        route = "/calendar/add_event"
    elif res == "[6, 1]":
        route = "/calendar/remove_event"
    elif res == "[6, 2]":
        route = "/calendar/update_event"
    elif res == "[6, 3]":
        route = "/calendar/view_events"
    else:
        route = "Route not exist"
    
    message = f"You can import the API at route : {route}"
    return jsonify({'result': message})
      