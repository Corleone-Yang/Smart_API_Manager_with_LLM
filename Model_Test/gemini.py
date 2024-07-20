import requests
import json

# Load test data
with open('data/test.json') as f:
    test_data = json.load(f)

# Due to the API requests limit, I split the whole data into two parts
test_data = test_data[10:]

# Load the prompt
with open('data/prompt.txt') as f:
    prompt = f.read()

# Set Google API key
api_key = "Your_Google_Gemini_API"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

# Initialize mismatch counter
count_mismatch = 0

# Define a function to extract classification from the generated text
def extract_classification(generated_text):
    # Assume the classification result is on the last line of the generated text
    return generated_text.strip().split('\n')[-1]

# Standardize function: Remove whitespace and convert to string
def standardize_classification(classification):
    return str(classification).strip()

# Inference and comparison
for item in test_data:
    query = item['query']
    expected_classification = item['classification']
    
    # Combine prompt and query
    input_text = f"{prompt}\nQuery: {query}\nClassification:"

    # Prepare the payload
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": input_text}
                ]
            }
        ]
    }

    # Perform inference
    response = requests.post(url, headers={'Content-Type': 'application/json'}, json=payload)
    response_json = response.json()
    
    # Debugging: print the response JSON
    print(f"Response JSON for query '{query}': {response_json}")

    # Extract parts and text content
    parts = response_json.get('candidates', [{}])[0].get('content', {}).get('parts', [])
    text_content = ''.join(part.get('text', '') for part in parts)
    
    # Debugging: print the extracted text content
    print(f"Extracted text content for query '{query}': {text_content}")
    
    # Extract classification from the generated text
    predicted_classification = extract_classification(text_content)
    
    # Debugging: print the predicted classification
    print(f"Predicted classification for query '{query}': {predicted_classification}")
    
    # Compare standardized results
    if standardize_classification(predicted_classification) != standardize_classification(expected_classification):
        count_mismatch += 1
        print(f"Mismatch for query: {query}")
        print(f"Expected: {expected_classification}, Got: {predicted_classification}")

# Print total mismatch count
print(f"Total mismatches: {count_mismatch}")
