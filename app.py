import streamlit as st
from chatbot import get_chatbot_response

st.set_page_config(page_title="CDP Support Chatbot", page_icon="🤖", layout="wide")

st.title("Support Agent Chatbot 🎖️")
st.write("Powered By Groq")
st.write("Ask me how-to questions about Segment, mParticle, Lytics, or Zeotap!")
st.write("Made By Indranil Bain")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize session state for conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Sidebar for conversation history
with st.sidebar:
    st.subheader("Conversation History")
    if st.session_state.conversation:
        for i, chat in enumerate(st.session_state.conversation):
            st.markdown(f"**Q{i+1}:** {chat['question']}")
            st.markdown(f"**A{i+1}:** {chat['answer']}")
            st.markdown("---")
    else:
        st.write("No history yet.")

    # Clear conversation history
    if st.button("Clear History"):
        st.session_state.conversation = []
        st.success("Conversation history cleared!")

# Main content area for the most recent question and answer
st.subheader("Ask a Question")
question = st.text_area("Enter your question:", placeholder="How do I set up a new source in Segment?")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            try:
                # Get the chatbot's response
                response = get_chatbot_response(question, GROQ_API_KEY)

                # Add the question and response to the conversation history
                st.session_state.conversation.append({"question": question, "answer": response})

                # Display the most recent question and answer at the top
                st.subheader("Most Recent Question and Answer")
                st.markdown(f"**Question:** {question}")
                st.markdown(f"**Answer:** {response}")

            except Exception as e:
                st.error(f"An error occurred: {e}")