from flask import Flask, request, jsonify
import openai  # Import the OpenAI library
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app) 

openai.api_key = os.environ.get('openaii') #jibran


story1 = """
name of company is WebTose 
Welcome to WebTose – Where Digital Dreams Come to Life!

In the heart of innovation, WebTose stands as a beacon for businesses seeking unparalleled excellence in website development and AI chatbot services. Let us take you on a journey of digital transformation, where your ideas evolve into captivating online experiences.

Once upon a time, in the bustling realm of the internet, there was a visionary company named WebTose. With a team of dedicated professionals driven by a passion for technology, WebTose emerged as a leader in crafting bespoke websites and implementing cutting-edge AI chatbot solutions.

Our Website Development Wizards:
Picture a team of skilled developers at WebTose, weaving intricate codes to build the digital face of your brand. From sleek portfolios that dazzle to powerful e-commerce platforms that sell, our wizards specialize in bringing your website dreams to reality. Each website is a unique masterpiece, reflecting the essence of your brand and capturing the attention of your online audience.

The AI Chatbot Alchemists:
In the enchanted laboratory of WebTose, our AI Chatbot Alchemists work tirelessly to infuse intelligence into your customer interactions. These magical chatbots, tailored to your business needs, provide seamless and personalized experiences. Watch as automation transforms your customer support, providing instant responses and ensuring your users feel a connection with your brand.

Why Choose the WebTose Adventure?
- Expertise Beyond Boundaries: Our team of seasoned professionals possesses a wealth of experience in both website development and the realm of AI.
- Pioneering Innovation: Navigate the digital landscape with confidence, as WebTose pioneers innovative solutions that keep you ahead of the curve.
- Your Success, Our Priority: At WebTose, we thrive on your success. Our customer-centric approach ensures that every solution aligns with your goals and aspirations.

Contacting the Digital Guides:
📞 Phone: +923308138077
📧 Email: info@webtose.com
🌐 Website: www.webtose.com

Embark on Your Digital Odyssey:
Ready to embark on a digital adventure? Contact WebTose today for a consultation. Let's embark on a journey where your online presence transforms into a captivating story of success!
"""

 
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
    if question.lower() == "hey":
        return "Welcome to our website! How may I help you?"
    elif "how are you" in question.lower():
        return "I'm just a computer program, but thanks for asking!" 
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

def ask_question_webtose(question):
    if question.lower() == "hey":
        return "Welcome to our website! How may I help you?"
    elif "how are you" in question.lower():
        return "I'm just a computer program, but thanks for asking!" 
    prompt = f"The story is: {story1}\nQuestion: {question}"

   
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
 

@app.route('/webtose', methods=['POST'])
def ask_question_webtose():
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
