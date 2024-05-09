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
import io
import base64
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
import wave
import asyncio
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from bson import json_util
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from flask_cors import CORS
from bson import ObjectId
 
 


    
os.environ.get('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)
 


# Set up MongoDB client and collection
client = MongoClient('mongodb+srv://jibran:jibranmern@clusterone.u74t8kf.mongodb.net/?retryWrites=true&w=majority')
DB_NAME = "AIBanker"
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
# prompt_template = """Use the following pieces of context to answer the question at 
# the end. If you don't know the answer, just say that you don't know only, don't try to make up an answer. 
# -Importtant:Please give the response of 1 line only for, . if answer is not found in context, try to get relavent
#  answer but it should be from context, not from all over the world, you can also suggest the user 
#  that are you asking for this you are AI Banker".

prompt_template = """Please utilize the provided context to answer the question below. If the answer is 
not available within the context, provide a relevant response based solely on the provided information. 
Refrain from inventing answers. If uncertain, simply state "I don't know". 
-Important: Kindly limit your response to one line only. Additionally, if necessary, you may remind the user 
that you are an AI Banker and suggest narrowing the question within the given context. Greet the user like human if they greet you."

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

# List to store previous _id values
previous_ids = []

# API Endpoint for chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if 'query' not in data:
        return jsonify({"error": "No 'query' provided"}), 400

    query = data['query']
    docs = qa({"query": query})

    # Convert the Document object to JSON serializable format
    return jsonify(docs["result"])

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    data = request.get_json()
    if 'pdf_base64' not in data:
        return jsonify({'error': 'No PDF data found'})

    pdf_base64 = data['pdf_base64']

    # Decode base64 to bytes
    pdf_bytes = base64.b64decode(pdf_base64)

    # Save PDF bytes to a temporary file
    temp_pdf_path = 'temp.pdf'
    with open(temp_pdf_path, 'wb') as temp_pdf:
        temp_pdf.write(pdf_bytes)

    # Load the PDF from the temporary file
    loader = PyPDFLoader(temp_pdf_path)
    pdf_data = loader.load()

    # Split the document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(pdf_data)

    # Insert documents into MongoDB with embeddings
    try:
        vector_search_instance = MongoDBAtlasVectorSearch.from_documents(
            documents=docs,
            embedding=OpenAIEmbeddings(disallowed_special=()),
            collection=MONGODB_COLLECTION,
            index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
        )
    except Exception as e:
        # Handle specific errors
        error_message = str(e)
        return jsonify({'error': error_message}), 500

    # Retrieve the _id of the previous document
    previous_ids = []
    previous_document = MONGODB_COLLECTION.find().sort('_id', -1).limit(1)
    for doc in previous_document:
      previous_id = str(doc['_id'])  # Convert ObjectId to string
      previous_ids.append(previous_id)
      print(previous_id)
  
# Remove the temporary file
    os.remove(temp_pdf_path)

# Return JSON response
    return jsonify({'message': 'PDF processed and inserted into MongoDB with embeddings!', 'previous_id': previous_ids[0]})

@app.route('/delete_all_documents', methods=['DELETE'])
def delete_all_documents():
    try:
        # Delete all documents from the 'document' collection
        result = MONGODB_COLLECTION.delete_many({})
        deleted_count = result.deleted_count
        return jsonify({'message': f'Deleted {deleted_count} documents from {COLLECTION_NAME} collection'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/display_previous_ids', methods=['GET'])
def display_previous_ids():
    # Display the list of previous _id values in the console
    print("Previous _id values:", previous_ids)
    return jsonify({'previous_ids': previous_ids})

@app.route('/', methods=['GET'])
def home():
    return "Server is running"












 












# if __name__ == '__main__':
#     app.run()
