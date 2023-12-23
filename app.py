from flask import Flask, request, jsonify
import openai  # Import the OpenAI library
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app) 

openai.api_key = os.environ.get('openaii') #jibran


#story = """there was a boy whose name is jibran he is a mern stack developer"""
 
story = """
Welcome to The IK Agency, your premier partner for cutting-edge Social Media Marketing and Management (SMMA) services. 
At The IK Agency, we pride ourselves on delivering innovative solutions to enhance your online presence, engage your audience, and drive measurable results.

About Us:
The IK Agency is a team of dedicated professionals passionate about helping businesses thrive in the digital landscape. 
With years of experience in the industry, we understand the dynamic nature of social media and leverage the latest trends to elevate your brand.

Our Services:
- Social Media Strategy: Tailored strategies to align with your business goals and target audience.
- Content Creation: Compelling and shareable content that resonates with your audience.
- Community Management: Building and nurturing your online community for sustained growth.
- Analytics and Reporting: Data-driven insights to measure success and inform future strategies.

Why Choose The IK Agency?
- Proven Results: Our track record speaks for itself, with success stories across various industries.
- Innovative Approach: Stay ahead of the competition with our forward-thinking strategies.
- Client-Centric Focus: Your success is our priority, and we work closely with you to achieve your objectives.

Contact Information:
Phone: +852 6439 4061
Email: info@theikagency.com
Owner: Grace Kim

Get in Touch:
Ready to take your social media presence to the next level? Contact The IK Agency today for a consultation. Let's turn your social media channels into powerful tools for growth.
"""
 
def answer_question(question):
    
    prompt = f"The story is: {story}\nQuestion: {question}"

   
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000
    )

 
    answer = response.choices[0].text.strip()

    prefixes_to_remove = ["?\n\nAnswer:", "?"]
    for prefix in prefixes_to_remove:
        if answer.startswith(prefix):
            answer = answer[len(prefix):].strip()
    if not answer:
        answer = generate_gpt_response(question)     

   
    return answer
 
def generate_gpt_response(question):
    # You can use the GPT-3.5 model here to generate a response for the question
    # You may need to adapt this part based on your GPT-3.5 implementation
    # For simplicity, you can use OpenAI's GPT-3 Python library
    gpt_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens=1000
    )

    return gpt_response.choices[0].text.strip()


 
@app.route('/', methods=['GET'])
def start():
    print('Starting Server')
    return 'Server is running'

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question', '')
    answer = answer_question(question)
    return jsonify({ 'answer': answer})
 




 
# from flask import Flask


# app = Flask(__name__)

 
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'
