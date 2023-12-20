from flask import Flask, request, jsonify
import openai  # Import the OpenAI library

app = Flask(__name__)

 
openai.api_key = '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'

 
story = """Once upon a time in a small village, there lived a young girl named Lily. 
She was known for her love of nature and spent her days exploring the outskirts of the village. 
One day, while wandering through the dense forest, Lily stumbled upon a hidden path that led her to a mysterious garden. 
The garden was unlike anything Lily had ever seen. Vibrant flowers of every color imaginable bloomed in perfect harmony, 
and the air was filled with the sweet scent of blossoms. Intrigued, Lily decided to explore further and discovered a small pond at the heart of the garden. 
As she approached, a magical creature emerged from the water – a talking frog named Oliver. 
Oliver explained that the garden was enchanted, and only those with pure hearts could find it. 
Lily, being kind-hearted and curious, was welcomed by the magical inhabitants of the garden. 
She spent her days talking to the animals, learning about the secrets of the enchanted realm, and even befriending a wise old owl. 
However, the enchantment came with a condition. Lily had to keep the garden a secret and not reveal its location to anyone with a wicked heart. 
The magical beings explained that the garden's existence depended on its secrecy, and if it was exposed to the wrong person, the enchantment would fade away. 
Days turned into weeks, and Lily's heart swelled with joy as she continued to cherish the magical haven. 
But one day, a sly and selfish villager named Edgar overheard Lily talking about the enchanted garden. 
Greed overtook him, and he decided to find it for himself, hoping to use its magic for personal gain."""

 
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

 










