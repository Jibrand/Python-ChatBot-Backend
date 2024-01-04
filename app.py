from flask import Flask, request, jsonify
import openai  # Import the OpenAI library
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app) 

openai.api_key = os.environ.get('openaii') #jibran

story3 = """ Legacy Wealth Co LLC - Elevating Your Financial Future

Empower Your Wealth Journey with Mark Cassara

Financial Coaching | Wealth Strategies | Life Insurance | Retirement Planning | Tax Strategies | Risk Minimization

About Mark Cassara and Legacy Wealth Co LLC:

Who is Mark Cassara?
Mark Cassara is more than just a financial coach and wealth strategist; he is your dedicated partner in navigating the complexities of financial planning. With a career spanning years, Mark has honed his skills to become a trusted advisor, committed to helping individuals achieve financial success and security.

What is Legacy Wealth Co LLC?
Legacy Wealth Co LLC stands as a testament to Mark Cassara's commitment to providing holistic financial solutions. It is a results-driven firm, dedicated to assisting clients in North Texas and beyond in achieving their financial goals and creating a lasting legacy for generations to come.

Services Offered:

What services does Legacy Wealth Co LLC provide?

Financial Coaching:
Mark Cassara understands that financial literacy is the cornerstone of informed decision-making. Our financial coaching services go beyond traditional advisory roles. Mark provides personalized coaching sessions to empower clients with practical knowledge and skills in budgeting, debt management, and investment strategies. Whether you are a seasoned investor or a financial novice, our coaching sessions are tailored to meet your unique needs and help you build a solid foundation for financial success.

Wealth Strategies:
Tailoring strategies to your unique circumstances, Legacy Wealth Co LLC works closely with clients to develop comprehensive wealth management plans. This includes analyzing current financial situations, setting short-term and long-term goals, and crafting personalized strategies for investments, asset allocation, and wealth preservation. Our goal is to guide clients toward financial independence and sustained growth, ensuring their wealth works for them.

Life Insurance:
As a specialist in life insurance, Mark Cassara offers a suite of comprehensive coverage options to meet diverse needs:

Indexed Universal Life (IUL): Providing flexibility and potential cash value growth, IULs offer a unique balance of protection and wealth accumulation.

●	Whole Life Insurance: Beyond just coverage, Whole Life policies provide a lifetime of benefits, including a guaranteed death benefit and the accumulation of cash value over time.

●	Infinite Banking: Leveraging life insurance policies for personal financing needs, Infinite Banking allows clients to access cash values for various purposes, offering a unique approach to wealth management. Mark tailors each life insurance solution to align with individual financial goals, family dynamics, and legacy planning.

Retirement Planning: Legacy Wealth Co LLC takes a holistic approach to retirement planning, going beyond traditional strategies. Mark Cassara collaborates with clients to develop personalized retirement plans that consider lifestyle goals, healthcare needs, and legacy planning. From analyzing pension options to optimizing Social Security benefits, our retirement planning services are designed to provide clients with confidence in their post-career financial security.

Tax Strategies: Navigating the complexities of the tax landscape requires proactive strategies. Mark Cassara helps clients minimize tax liabilities and optimize their financial position through:

●	Tax-Efficient Investing: Implementing investment strategies that aim to reduce tax consequences.
●	Strategic Deductions: Identifying opportunities for deductions and credits to enhance overall tax efficiency.
●	Retirement Account Optimization: Maximizing the benefits of retirement accounts to minimize tax burdens. 
Legacy Wealth Co LLC ensures that clients have a tax-efficient financial plan, enabling them to keep more of their hard-earned money.

Risk Minimization: Safeguarding financial well-being involves strategic planning and risk mitigation. Legacy Wealth Co LLC assists clients in minimizing risks through:

●	Diversification Strategies: Spreading investments across different asset classes to reduce exposure to specific risks.
●	Insurance Planning: Assessing and implementing appropriate insurance coverage to protect against unforeseen events.
●	Emergency Fund Management: Establishing and managing emergency funds to mitigate the impact of unexpected financial challenges.

Mark Cassara guides clients in navigating uncertainties and building resilience in their financial plans.

Specialization and Expertise:

What makes Legacy Wealth Co LLC stand out?
Mark Cassara's specialization in advanced policy design sets Legacy Wealth Co LLC apart:

Indexed Universal Life (IUL): Beyond basic life insurance, IULs offer flexibility and the potential for cash value growth. Mark tailors these policies to suit individual financial goals.

Whole Life Insurance: Providing not just coverage but a lifetime of benefits, Whole Life policies ensure financial security and the accumulation of cash value over time.

Infinite Banking: Mark leverages life insurance policies for personal financing needs, offering clients a unique approach to managing and growing their wealth.

Fixed Indexed Annuities: Striking a balance between growth potential and downside protection, these annuities provide a reliable source of income in retirement.

Join Our Team:

Is Legacy Wealth Co LLC hiring?
Yes, Legacy Wealth Co LLC is actively seeking motivated individuals to join its team. The firm believes in the power of collaboration and is dedicated to nurturing talent within the financial services industry.

How can I become a part of Legacy Wealth Co LLC?
If you are passionate about helping others achieve financial success and are interested in a fulfilling career in financial services, reach out to Mark Cassara. Explore the exciting opportunities available and contribute to the legacy of helping individuals secure their financial future.

Contact Information:

For inquiries, consultations, or career opportunities, please contact Mark Cassara at:

Legacy Wealth Co LLC
legacywealthco.com

Mark Cassara
mark@legacywealthco.com

At Legacy Wealth Co LLC, we don't just offer services; we provide a roadmap to financial empowerment. Let us be your partner in building a secure and lasting legacy.


Frequently Asked Questions (FAQs):
	Q: What sets Legacy Wealth Co LLC apart from other financial firms?
●	A: Legacy Wealth Co LLC, led by Mark Cassara, stands out for its holistic approach to financial planning. We offer personalized coaching, comprehensive wealth strategies, and specialization in advanced policy design, setting us apart as a partner committed to your long-term financial success.
	Q: What can I expect from financial coaching sessions with Mark Cassara?
●	A: Our financial coaching sessions are tailored to your unique needs. Mark provides practical knowledge and skills in budgeting, debt management, and investment strategies. Whether you're a seasoned investor or just starting, our coaching aims to empower you with the tools for financial success.
	Q: What types of life insurance does Legacy Wealth Co LLC specialize in?
●	A: Mark Cassara specializes in various life insurance options, including Indexed Universal Life (IUL), Whole Life, and Infinite Banking. Each solution is customized to meet individual goals, family dynamics, and legacy planning.
	Q: How does Infinite Banking work, and how can it benefit me?
●	A: Infinite Banking leverages life insurance policies for personal financing needs. It allows you to access cash values for various purposes, providing flexibility and control over your financial resources. Mark Cassara can guide you on how this strategy can benefit your specific financial situation.
	Q: What is the significance of comprehensive wealth strategies at Legacy Wealth Co LLC?
●	A: Our comprehensive wealth strategies involve analyzing your current financial situation, setting short-term and long-term goals, and crafting personalized plans for investments, asset allocation, and wealth preservation. The goal is to guide you toward financial independence and sustained growth.
	Q: How does Legacy Wealth Co LLC approach retirement planning differently?
●	A: Our retirement planning goes beyond traditional strategies. Mark Cassara collaborates with clients to develop personalized plans, considering lifestyle goals, healthcare needs, and legacy planning. From pension analysis to Social Security optimization, we ensure a holistic approach to post-career financial security.
	Q: What tax strategies does Legacy Wealth Co LLC implement for clients?
●	A: Mark Cassara helps clients minimize tax liabilities and optimize their financial position through tax-efficient investing, strategic deductions, and retirement account optimization. Our goal is to create a tax-efficient financial plan, allowing you to keep more of your hard-earned money.
	Q: How does Legacy Wealth Co LLC assist in risk minimization?
●	A: We help clients minimize risks through diversification strategies, insurance planning, and emergency fund management. Mark Cassara guides clients in navigating uncertainties and building resilience in their financial plans.
	Q: Is Legacy Wealth Co LLC currently hiring?
●	A: Yes, Legacy Wealth Co LLC is actively seeking motivated individuals to join our team. If you are passionate about helping others achieve financial success, reach out to Mark Cassara to explore exciting career opportunities.
	Q: How can I contact Mark Cassara for a consultation or inquiry?
●	A: You can reach out to Mark Cassara for consultations, inquiries, or career opportunities through the provided contact information:
●	Legacy Wealth Co LLC
legacywealthco.com

●	Mark Cassara
mark@legacywealthco.com

Calendar link for a free financial strategy call: https://link.legsysbldr.co/widget/booking/QDb6ojk94Ctmsg2bgSLP

Calendar link to a recruiting interview: https://link.legsysbldr.co/widget/booking/xwh9kePZ5A85IDKF6XWv 


Marks Social Media Links:
https://www.tiktok.com/@markcassara
https://www.instagram.com/realmarkcassara/
https://www.facebook.com/mccassara
https://twitter.com/markcassara
https://youtube.com/@markcassara

"""
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



def answer_question_wordpress(question):
  
     
    prompt = f"The story is: {story3}\nQuestion: {question}"

   
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

def answer_question_webtose(question):
  
    
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
    answer = answer_question_webtose(question)
    return jsonify({ 'answer': answer})

@app.route('/legacy', methods=['POST'])
def answer_question_wordpress():
    data = request.get_json()
    question = data.get('question', '')
    answer = answer_question_wordpress(question)
    return jsonify({ 'answer': answer})
 
# from flask import Flask


# app = Flask(__name__)

 
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'
