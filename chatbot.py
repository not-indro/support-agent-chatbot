from groq import Groq

def get_chatbot_response(question, groq_api_key):
    """
    Generate a response using the Groq API.
    """
    # Initialize Groq client
    client = Groq(api_key=groq_api_key)

    # Combine all documentation into a single context
    context = ""  # Add your logic to build the context here

    # Generate a response using Groq API
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
        model="llama-3.3-70b-versatile",  # Use the desired Groq model
    )
    return chat_completion.choices[0].message.content