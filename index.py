from flask import Flask, request, jsonify
import openai  # Import the OpenAI library

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

# Define the pre-defined story
story = """Once upon a time in a small village, there lived a young girl named Lily"""

# Function to answer questions about the story
def answer_question(question):
    # Prepare the prompt for OpenAI API
    prompt = f"The story is: {story}\nQuestion: {question}"

    # Send the prompt to OpenAI API and get the response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
    )

    # Extract the answer from the response
    answer = response.choices[0].text.strip()

    # Return the answer
    return answer

# API endpoint to handle questions
@app.route('/', methods=['GET'])
def start():
    print('Starting Server')
    return 'Server is running'

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question', '')
    answer = answer_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
