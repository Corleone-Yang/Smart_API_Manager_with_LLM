import json
from huggingface_hub import InferenceClient

# Load test data
with open('data/test.json') as f:
    test_data = json.load(f)

# Due to the API requests limit, I split the whole data into two parts
test_data = test_data[600:]

# Load the prompt
with open('data/prompt.txt') as f:
    prompt = f.read()

# Create Huggingface Inference Client
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token="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"
)

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

    # Perform inference
    response = client.chat_completion(
        messages=[{"role": "user", "content": input_text}],
        max_tokens=10,
        stream=False,
    )
    
    # Check if response is in the expected format
    if isinstance(response, dict) and 'choices' in response and len(response['choices']) > 0:
        generated_text = response['choices'][0]['message']['content']
    else:
        print(f"Unexpected response format: {response}")
        continue
    
    # Extract classification from the generated text
    predicted_classification = extract_classification(generated_text)
    
    # Compare standardized results
    if standardize_classification(predicted_classification) != standardize_classification(expected_classification):
        count_mismatch += 1
        print(f"Mismatch for query: {query}")
        print(f"Expected: {expected_classification}, Got: {predicted_classification}")

# Print total mismatch count
print(f"Total mismatches: {count_mismatch}")
