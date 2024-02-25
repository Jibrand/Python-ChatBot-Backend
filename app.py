# from flask import Flask, request, jsonify
# import openai  # Import the OpenAI library
# from flask_cors import CORS 
# import os

# app = Flask(__name__)
# CORS(app) 

# openai.api_key = os.environ.get('openaii') #jibra


# conversation_history = "" 


# story1 = """
# name of company is WebTose 
# Welcome to WebTose – Where Digital Dreams Come to Life.

# In the heart of innovation, WebTose stands as a beacon for businesses seeking unparalleled excellence in website development and AI chatbot services. Let us take you on a journey of digital transformation, where your ideas evolve into captivating online experiences.

# Once upon a time, in the bustling realm of the internet, there was a visionary company named WebTose. With a team of dedicated professionals driven by a passion for technology, WebTose emerged as a leader in crafting bespoke websites and implementing cutting-edge AI chatbot solutions.

# Our Website Development Wizards:
# Picture a team of skilled developers at WebTose, weaving intricate codes to build the digital face of your brand. From sleek portfolios that dazzle to powerful e-commerce platforms that sell, our wizards specialize in bringing your website dreams to reality. Each website is a unique masterpiece, reflecting the essence of your brand and capturing the attention of your online audience.

# The AI Chatbot Alchemists:
# In the enchanted laboratory of WebTose, our AI Chatbot Alchemists work tirelessly to infuse intelligence into your customer interactions. These magical chatbots, tailored to your business needs, provide seamless and personalized experiences. Watch as automation transforms your customer support, providing instant responses and ensuring your users feel a connection with your brand.

# Why Choose the WebTose Adventure?
# - Expertise Beyond Boundaries: Our team of seasoned professionals possesses a wealth of experience in both website development and the realm of AI.
# - Pioneering Innovation: Navigate the digital landscape with confidence, as WebTose pioneers innovative solutions that keep you ahead of the curve.
# - Your Success, Our Priority: At WebTose, we thrive on your success. Our customer-centric approach ensures that every solution aligns with your goals and aspirations.

# Contacting the Digital Guides:
# 📞 Phone: +923308138077
# 📧 Email: info@webtose.com
# 🌐 Website: www.webtose.com

# Embark on Your Digital Odyssey:
# Ready to embark on a digital adventure? Contact WebTose today for a consultation. Let's embark on a journey where your online presence transforms into a captivating story of success!
# """

# def answer_question_webtose(question):
#     global conversation_history
    
#     prompt = f"The story is: {story1}\nConversation History: {conversation_history}\nQuestion: {question}"

#     response = openai.completions.create(
#         model="gpt-3.5-turbo-instruct",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=1000
#     )
 
#     answer = response.choices[0].text.strip()

#     prefixes_to_remove = ["?\n\nAnswer:", "?"]
#     for prefix in prefixes_to_remove:
#         if answer.startswith(prefix):
#             answer = answer[len(prefix):].strip()
#     if not answer:
#         answer = generate_gpt_response(question)     
    
#     conversation_history += f"\nUser: {question}\nAI: {answer}"

#     return answer

 

 
# def generate_gpt_response(question):
 
#     gpt_response = openai.Completion.create(
#         model="gpt-3.5-turbo-instruct",
#         prompt=question,
#         temperature=0.7,
#         max_tokens=1000
#     )

#     return gpt_response.choices[0].text.strip()
 
# @app.route('/', methods=['GET'])
# def start():
#     print('Starting Server')
#     return 'Server is running'


# @app.route('/webtose', methods=['POST'])
# def ask_question_webtose():
#     try:
#         data = request.get_json()
#         question = data.get('question', '')
#         answer = answer_question_webtose(question)
#         return jsonify({'answer': answer})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# #if __name__ == '__main__':
#     #app.run(debug=True)



from flask import Flask, request, jsonify
from pymongo import MongoClient
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from bson import json_util
import os
from flask_cors import CORS  # Import CORS


os.environ["OPENAI_API_KEY"] = 'xz'

app = Flask(__name__)
CORS(app)

# Set up MongoDB client and collection
client = MongoClient('mongodb+srv://jibran:jibranmern@clusterone.u74t8kf.mongodb.net/?retryWrites=true&w=majority')
DB_NAME = "test"
COLLECTION_NAME = "document"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

# Initialize MongoDBAtlasVectorSearch
vector_search = MongoDBAtlasVectorSearch(
    embedding=OpenAIEmbeddings(disallowed_special=()),
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)

# Initialize QA Retriever
qa_retriever = vector_search.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 25},
)

# Prompt Template
prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know only, don't try to make up an answer. if you questioned about your name tell Your name is AI Banker only dont tell you dont have name

{context}

Question: "{question}"
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Initialize QA Chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=qa_retriever,
    # return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT},
)

# API Endpoint for chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if 'query' not in data:
        return jsonify({"error": "No 'query' provided"}), 400

    query = data['query']
    docs = qa({"query": query})

    # Convert the Document object to JSON serializable format
    print (data)
    print (query)
    print(docs["result"])
    return jsonify(docs["result"])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


