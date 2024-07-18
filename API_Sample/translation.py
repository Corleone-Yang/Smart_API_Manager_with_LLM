from flask import Blueprint, request, jsonify
import openai
import os

translation = Blueprint('translation', __name__)

# set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@translation.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({"error": "Please provide both text and target_language"}), 400

    try:
        #  Call the OpenAI API to translate the text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Translate the following text to {target_language}: {text}",
            max_tokens=1000
        )
        translation = response.choices[0].text.strip()
        return jsonify({"translation": translation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
