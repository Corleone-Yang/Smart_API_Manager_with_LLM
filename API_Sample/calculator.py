from flask import Blueprint, request, jsonify
import math

calculator = Blueprint('calculator', __name__)

@calculator.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'result': result})

@calculator.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify({'result': result})

@calculator.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({'result': result})

@calculator.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    result = data['a'] / data['b']
    return jsonify({'result': result})

@calculator.route('/power', methods=['POST'])
def power():
    data = request.get_json()
    result = data['a'] ** data['b']
    return jsonify({'result': result})

@calculator.route('/sqrt', methods=['POST'])
def sqrt():
    data = request.get_json()
    result = data['a'] ** 0.5
    return jsonify({'result': result})

@calculator.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    result = math.log(data['a'], data['b'])
    return jsonify({'result': result})

@calculator.route('/factorial', methods=['POST'])
def factorial():
    data = request.get_json()
    result = math.factorial(data['a'])
    return jsonify({'result': result})

@calculator.route('/sin', methods=['POST'])
def sin():
    data = request.get_json()
    result = math.sin(data['a'])
    return jsonify({'result': result})

@calculator.route('/cos', methods=['POST'])
def cos():
    data = request.get_json()
    result = math.cos(data['a'])
    return jsonify({'result': result})

@calculator.route('/tan', methods=['POST'])
def tan():
    data = request.get_json()
    result = math.tan(data['a'])
    return jsonify({'result': result})

