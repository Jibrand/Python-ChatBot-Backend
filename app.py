from flask import Flask, request, jsonify
import openai  # Import the OpenAI library
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app) 

openai.api_key = os.environ.get('openaii') #jibran

conversation_history = "" 


story1 = """
name of company is WebTose 
Welcome to WebTose – Where Digital Dreams Come to Life.

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

def answer_question_webtose(question):
    global conversation_history
    prompt = f"The story is: {story1}\nConversation History: {conversation_history}\nQuestion: {question}"

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
    
 
    conversation_history += f"\nUser: {question}\nAI: {answer}"

    return answer

 
def generate_gpt_response(question):
 
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


 @app.route('/webtose', methods=['POST'])
def ask_question_webtose():
    try:
        data = request.get_json()
        question = data.get('question', '')
        answer = answer_question_webtose(question)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# from flask import Flask
# app = Flask(__name__)
