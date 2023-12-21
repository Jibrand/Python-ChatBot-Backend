from flask import Flask, request, jsonify
import openai  # Import the OpenAI library
import os

app = Flask(__name__)


openai.api_key = os.environ.get('openaii') #jibran


story = """there was a boy whose name is jibran he is a mern stack developer"""
 

 
def answer_question(question):
    
    prompt = f"The story is: {story}\nQuestion: {question}"

   
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_token=1000,
        n=9,
        stream=False,
        stop=None,
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

 
 



