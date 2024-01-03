from flask import Flask, request, jsonify
import pathlib
import textwrap
import google.generativeai as genai

# Configure Generative AI API with your API key
GOOGLE_API_KEY = 'AIzaSyB3V7zRB-e6DfSocIiD8yIyWj5M8pcIRN0'  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Create a Generative Model instance
model = genai.GenerativeModel('gemini-pro')

# Define a function for Markdown formatting (optional)
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Create the Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    # Retrieve query from request data
    query = request.get_json().get('query')

    # Generate response using the model
    response = model.generate_content(query)

    # Format response as JSON (optional: apply Markdown formatting if needed)
    response_text = to_markdown(response)  # Uncomment if using Markdown formatting
    response_json = jsonify({'response_text': response_text})

    return response_json

# Run the API
# if __name__ == '__main__':
#     app.run(debug=True)
