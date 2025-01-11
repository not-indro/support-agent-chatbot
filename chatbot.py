import os
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()
# Access the API key from Streamlit Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

with open("cdp_docs.json", "r") as f:
    cdp_docs = json.load(f)

def filter_relevant_sections(question, docs):
    """
    Filter relevant sections of the documentation based on the user's question.
    """
    relevant_sections = []
    for doc in docs:
        if question.lower() in doc.lower():
            relevant_sections.append(doc)
    return relevant_sections

def truncate_context(context, max_tokens=90000):
    """
    Truncate the context to stay within the token limit.
    """

    if len(context) > max_tokens * 4:
        context = context[:max_tokens * 4]
    return context

def get_chatbot_response(question):
    context = ""
    for platform, docs in cdp_docs.items():
        relevant_sections = filter_relevant_sections(question, docs)
        for section in relevant_sections:
            chunks = chunk_text(section)
            for chunk in chunks:
                context += f"{platform.upper()} Documentation:\n{chunk}\n\n"
    
    context = truncate_context(context)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful support agent chatbot for Customer Data Platforms (CDPs)."
            },
            {
                "role": "user",
                "content": f"{question}\n\nContext:\n{context}"
            }
        ],
        model="llama-3.3-70b-versatile",  
    )
    return chat_completion.choices[0].message.content