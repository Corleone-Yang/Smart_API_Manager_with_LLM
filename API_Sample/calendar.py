from flask import Blueprint, request, jsonify

calendar = Blueprint('calendar', __name__)

class CalendarManagement:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, time, description):
        event = {
            'title': title,
            'date': date,
            'time': time,
            'description': description
        }
        self.events.append(event)
        return event

    def remove_event(self, index):
        if 0 <= index < len(self.events):
            return self.events.pop(index)
        else:
            return None

    def update_event(self, index, title=None, date=None, time=None, description=None):
        if 0 <= index < len(self.events):
            if title:
                self.events[index]['title'] = title
            if date:
                self.events[index]['date'] = date
            if time:
                self.events[index]['time'] = time
            if description:
                self.events[index]['description'] = description
            return self.events[index]
        else:
            return None

    def view_events(self):
        return self.events

calendar_service = CalendarManagement()

@calendar.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    result = calendar_service.add_event(data['title'], data['date'], data['time'], data['description'])
    return jsonify(result)

@calendar.route('/remove_event', methods=['DELETE'])
def remove_event():
    data = request.json
    result = calendar_service.remove_event(data['index'])
    return jsonify(result)

@calendar.route('/update_event', methods=['PUT'])
def update_event():
    data = request.json
    result = calendar_service.update_event(data['index'], data.get('title'), data.get('date'), data.get('time'), data.get('description'))
    return jsonify(result)

@calendar.route('/view_events', methods=['GET'])
def view_events():
    result = calendar_service.view_events()
    return jsonify(result)
