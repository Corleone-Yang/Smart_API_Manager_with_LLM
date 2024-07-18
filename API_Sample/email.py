from flask import Blueprint, request, jsonify

email = Blueprint('email', __name__)

class EmailManagement:
    def __init__(self):
        self.emails = []

    def compose_email(self, sender, recipient, subject, body):
        email = {
            'sender': sender,
            'recipient': recipient,
            'subject': subject,
            'body': body,
            'status': 'draft'
        }
        self.emails.append(email)
        return email

    def send_email(self, index):
        if 0 <= index < len(self.emails):
            self.emails[index]['status'] = 'sent'
            return self.emails[index]
        else:
            return None

    def read_email(self, index):
        if 0 <= index < len(self.emails):
            return self.emails[index]
        else:
            return None

    def delete_email(self, index):
        if 0 <= index < len(self.emails):
            return self.emails.pop(index)
        else:
            return None

email_service = EmailManagement()

@email.route('/compose_email', methods=['POST'])
def compose_email():
    data = request.json
    result = email_service.compose_email(data['sender'], data['recipient'], data['subject'], data['body'])
    return jsonify(result)

@email.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    result = email_service.send_email(data['index'])
    return jsonify(result)

@email.route('/read_email', methods=['GET'])
def read_email():
    index = int(request.args.get('index'))
    result = email_service.read_email(index)
    return jsonify(result)

@email.route('/delete_email', methods=['DELETE'])
def delete_email():
    data = request.json
    result = email_service.delete_email(data['index'])
    return jsonify(result)
