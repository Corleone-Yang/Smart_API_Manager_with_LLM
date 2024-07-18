import openai
import os

def classify_prompt(prompt):
    # get file path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'data', 'classification_rules.txt')

    with open(file_path, 'r') as file:
        classification_rules = file.read()

    # OpenAI API key setup
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Combine the classification rules with the user's prompt
    full_prompt = classification_rules + "\n" + prompt

    # Sending a prompt to the OpenAI API using the chat model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can choose the appropriate chat model
        messages=[{"role": "user", "content": full_prompt}]
    )

    # Extract and return the list from the response
    response_text = response['choices'][0]['message']['content'].strip()
    return response_text