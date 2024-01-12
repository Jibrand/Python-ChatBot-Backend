from flask import Flask, request, jsonify
import openai  # Import the OpenAI library
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app) 

openai.api_key = os.environ.get('openaii') #jibran
# openai.api_key = "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"


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

story_CalmHelper="""Welcome to CalmHelper – Where Digital Dreams Come to Life.

In the heart of innovation, CalmHelper stands as a beacon for individuals seeking unparalleled excellence in mental well-being support and AI-guided therapy. Let us take you on a journey of digital transformation, where your anxieties evolve into moments of calm and relaxation.

Once upon a time, in the bustling realm of the internet, there was a visionary companion named CalmHelper. With a team of dedicated professionals driven by a passion for mental health, CalmHelper emerged as a leader in providing support for anxiety, particularly the fear of heights.

Our Mindful Support Wizards:
Picture a team of skilled wizards at CalmHelper, weaving thoughtful guidance to address anxiety and height phobia. From personalized coping strategies to comforting conversations, our wizards specialize in bringing a sense of calm to your mental well-being. Each interaction is a unique journey, tailored to ease your worries and instill a sense of tranquility.

The Anxiety Alchemists:
In the serene laboratory of CalmHelper, our Anxiety Alchemists work tirelessly to infuse mindfulness into your daily life. These magical interactions, tailored to address specific fears like height phobia, provide a supportive and understanding presence. Experience as worries transform into moments of tranquility, providing instant relief and ensuring you feel a connection with your inner peace.

Why Choose the CalmHelper Journey?
- Expertise in Mindful Guidance: Our team of seasoned professionals possesses a wealth of experience in mental health support and the realm of AI-guided therapy.
- Pioneering Well-being Solutions: Navigate the landscape of your emotions with confidence, as CalmHelper pioneers innovative solutions that keep you grounded and centered.
- Your Peace of Mind, Our Priority: At CalmHelper, we thrive on contributing to your peace of mind. Our user-centric approach ensures that every interaction aligns with your emotional well-being goals and aspirations.

Connecting with CalmHelper:
📞 Phone: +923308138077
📧 Email: info@calmhelper.com
🌐 Website: www.calmhelper.com

Embark on Your Calm Journey:
Ready to embark on a digital journey towards calmness? Contact CalmHelper today for a consultation. Let's embark on a serene adventure where your mental well-being transforms into a story of peace and tranquility!
"""

question_example="""
User: Hello, I hope you're doing well. I've been feeling quite stressed lately.

Bot: Hi there! I'm here to help and listen. I'm sorry to hear that you're feeling stressed. It takes courage to reach out. Can you share a bit more about what's been going on?

User: Thank you. It's mainly work-related stress. I have tight deadlines, and it feels overwhelming.

Bot: I understand how demanding work can be. Meeting tight deadlines can indeed be stressful. How have you been coping with this pressure so far?

User: I've tried working longer hours, but it doesn't seem to help. I end up feeling exhausted.

Bot: It sounds like you're putting in a lot of effort. It's important to recognize the impact this is having on you. Have you considered taking short breaks during your workday to recharge?

User: I've thought about it, but there's so much to do. I feel like I can't take a break without falling behind.

Bot: I hear you. Balancing responsibilities can be challenging. Taking breaks doesn't necessarily mean falling behind. In fact, breaks can improve focus and productivity. Have you explored any specific relaxation techniques during these breaks?

User: I haven't really tried any relaxation techniques. What do you suggest?

Bot: There are various techniques you can explore, like deep breathing exercises, mindfulness, or even a short walk. Finding what works best for you is important. Would you like some guidance on a simple deep breathing exercise to start with?

User: Yes, that sounds helpful.

Bot: Great! Let's start with a deep breath. Inhale slowly for a count of four, hold for four, and exhale for four. Repeat this a few times, focusing on your breath. This can be a quick practice to ease tension. How does that feel?

User: I actually feel a bit more relaxed. Thanks for suggesting that.

Bot: You're welcome! I'm glad you found it helpful. Remember, it's okay to prioritize self-care. If you ever need someone to talk to or explore more strategies, I'm here for you. Additionally, consider discussing your workload concerns with your supervisor to find a sustainable solution.

User: Thank you for listening and the advice. I appreciate it.

Bot: It was my pleasure. Take care, and don't hesitate to reach out whenever you need support. Wishing you a less stressful day ahead! """

def answer_question_webtose(question):
    global conversation_history
    
    # prompt = f" Question: {question}"
    prompt = f"The story is: {story_CalmHelper}\nConversation History: {conversation_history}\nQuestion: {question}\nPlease allow me to assist you with utmost care and consideration\n you should have to very very much humble while answering, becasue you are the physiotherapist bot and you are dealing with mental health patients.\nPlease dont give too much big answer, i want the answer in one senence\nPLease ask questions related to question/patient problem. not just ask question, instead first give one kind sentence and speak humbly so that the the patient feel good then ask litttle bit question related to more get about his health, and how he got into this solution and give suitable answer/treatment\n dont use we, use I."
    # prompt = f"The story is: {story1}\nQuestion: {question}"

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
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

def answer_question_CalmHelper(question):
    global conversation_history
    
    # prompt = f" Question: {question}"
    prompt = f"The story is: {story1}\nConversation History: {conversation_history}\nQuestion: {question}\nPlease allow me to assist you with utmost care and consideration\n you should have to very very much humble while answering, becasue you are the physiotherapist bot and you are dealing with mental health patients.\nPlease"
    # prompt = f"The story is: {story1}\nQuestion: {question}"

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
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
        model="gpt-3.5-turbo-instruct",
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

@app.route('/CalmHelper', methods=['POST'])
def answer_question_CalmHelper():
    try:
        data = request.get_json()
        question = data.get('question', '')
        answer = answer_question_CalmHelper(question)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# if __name__ == '__main__':
#     app.run(debug=True)
