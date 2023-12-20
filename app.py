from flask import Flask, request, jsonify
import openai  # Import the OpenAI library

app = Flask(__name__)

 
openai.api_key = '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'

 
story = """Once upon a time in a small village, there lived a young girl named Lily"""

 
def answer_question(question):
    
    prompt = f"The story is: {story}\nQuestion: {question}"

   
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
    )

 
    answer = response.choices[0].text.strip()

   
    return answer

 
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
 




 
# from flask import Flask


# app = Flask(__name__)

 
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'

 









