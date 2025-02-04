# Support Agent Chatbot for CDPs

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=for-the-badge&logo=Playwright&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00A67E?style=for-the-badge&logo=Groq&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A **Support Agent Chatbot** that answers "how-to" questions related to four **Customer Data Platforms (CDPs)**: **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot extracts relevant information from the official documentation of these platforms to guide users on how to perform tasks or achieve specific outcomes.

---

## Features

- **Answer "How-to" Questions**:
  - Responds to user questions about how to perform tasks or use features within each CDP.
  - Example: "How do I set up a new source in Segment?"

- **Extract Information from Documentation**:
  - Retrieves relevant information from the official documentation of the four CDPs.

- **Handle Variations in Questions**:
  - Handles variations in question phrasing and terminology, including long or irrelevant questions.

- **Cross-CDP Comparisons**:
  - Answers questions about the differences in approaches or functionalities between the four CDPs.
  - Example: "How does Segment's audience creation process compare to Lytics'?"

- **Advanced "How-to" Questions**:
  - Handles complex or platform-specific "how-to" questions.
  - Example: "How do I integrate my data with Zeotap?"

---

## Technologies Used

- **Web Scraping**: [Playwright](https://playwright.dev/) (for dynamic websites), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) (for static content).
- **Natural Language Processing**: [Groq API](https://groq.com/) (`llama-3.3-70b-versatile`).
- **Web Framework**: [Streamlit](https://streamlit.io/) for the user interface.
- **Programming Language**: Python.
- **Data Storage**: JSON for storing scraped documentation.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/not-indro/support-agent-chatbot.git
   cd support-agent-chatbot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add your Groq API key:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key_here
     ```

---

## Usage

### Step 1: Scrape Documentation
Run the scraping script to extract documentation from the four CDPs:
```bash
python scrape_docs.py
```
This will create a `cdp_docs.json` file containing the scraped documentation.

### Step 2: Run the Chatbot
Start the Streamlit app to interact with the chatbot:
```bash
streamlit run app.py
```

### Step 3: Ask Questions
- Enter your question in the text area and click **Submit**.
- The chatbot will generate a response based on the scraped documentation.
- The conversation history (last 3 questions and answers) is displayed in the sidebar.

---

## Project Structure

```
support-agent-chatbot/
│
├── app.py                # Streamlit app for the chatbot interface
├── chatbot.py            # Chatbot logic using Groq API
├── scrape_docs.py        # Script to scrape documentation using Playwright
├── cdp_docs.json         # Scraped documentation (generated after running scrape_docs.py)
├── .env                  # Environment variables (e.g., Groq API key)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Playwright](https://playwright.dev/) for browser automation.
- [Groq](https://groq.com/) for the powerful LLM API.
- [Streamlit](https://streamlit.io/) for the user interface.
