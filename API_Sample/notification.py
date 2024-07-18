from flask import Blueprint, request, jsonify

notification = Blueprint('notification', __name__)

class Notification:
    def __init__(self):
        self.notifications = []

    def send_notification(self, user_id, message):
        notification = {
            'user_id': user_id,
            'message': message,
            'read': False
        }
        self.notifications.append(notification)
        return notification

    def view_notifications(self, user_id):
        return [notification for notification in self.notifications if notification['user_id'] == user_id]

    def mark_as_read(self, user_id, index):
        user_notifications = self.view_notifications(user_id)
        if 0 <= index < len(user_notifications):
            user_notifications[index]['read'] = True
            return user_notifications[index]
        else:
            return None

    def delete_notification(self, user_id, index):
        user_notifications = self.view_notifications(user_id)
        if 0 <= index < len(user_notifications):
            self.notifications.remove(user_notifications[index])
            return user_notifications[index]
        else:
            return None

notification_service = Notification()

@notification.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    result = notification_service.send_notification(data['user_id'], data['message'])
    return jsonify(result)

@notification.route('/view_notifications', methods=['GET'])
def view_notifications():
    user_id = request.args.get('user_id')
    result = notification_service.view_notifications(user_id)
    return jsonify(result)

@notification.route('/mark_as_read', methods=['POST'])
def mark_as_read():
    data = request.json
    result = notification_service.mark_as_read(data['user_id'], data['index'])
    return jsonify(result)

@notification.route('/delete_notification', methods=['DELETE'])
def delete_notification():
    data = request.json
    result = notification_service.delete_notification(data['user_id'], data['index'])
    return jsonify(result)
