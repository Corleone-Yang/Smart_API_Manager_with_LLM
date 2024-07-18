from flask import Blueprint, request, jsonify, current_app

notes = Blueprint('notes', __name__)

@notes.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    note = {
        'id': len(current_app.config['NOTES_DATA']) + 1,
        'title': data.get('title'),
        'content': data.get('content')
    }
    current_app.config['NOTES_DATA'].append(note)
    return jsonify({'result': 'Note created', 'note': note})

@notes.route('/all', methods=['GET'])
def get_all_notes():
    return jsonify({'notes': current_app.config['NOTES_DATA']})

@notes.route('/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = next((note for note in current_app.config['NOTES_DATA'] if note['id'] == note_id), None)
    if note:
        return jsonify({'note': note})
    else:
        return jsonify({'error': 'Note not found'}), 404

@notes.route('/delete/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    current_app.config['NOTES_DATA'] = [note for note in current_app.config['NOTES_DATA'] if note['id'] != note_id]
    return jsonify({'result': 'Note deleted'})

@notes.route('/update/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    note = next((note for note in current_app.config['NOTES_DATA'] if note['id'] == note_id), None)
    if note:
        note['title'] = data.get('title', note['title'])
        note['content'] = data.get('content', note['content'])
        return jsonify({'result': 'Note updated', 'note': note})
    else:
        return jsonify({'error': 'Note not found'}), 404


