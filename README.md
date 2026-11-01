# AI Text Summarizer

This is a simple AI Text Summarizer project built using Python, Streamlit, and the Groq API.

The application allows users to either paste text or upload a PDF file. It then generates a short summary in 3 bullet points using Groq.

## Features

- Summarize long text
- Upload and summarize PDF files
- Groq API integration
- Character count
- Simple and user-friendly interface

## Technologies Used

- Python
- Streamlit
- OpenAI Python SDK (with Groq's API endpoint)
- PyPDF2
- python-dotenv

## Project Structure

- app.py = Main file jisme Streamlit UI aur application ka logic hai.

- utils/groq.py = Groq API ko handle karta hai aur summary generate karta hai.

- utils/pdf_reader.py = Uploaded PDF se text extract karta hai.

- requirements.txt = Project me use hone wali libraries ki list.

- .env = Groq API key store karne ke liye (`.env.example` dekhein).

- .gitignore = Unnecessary files ko GitHub par upload hone se rokta hai.

- README.md = Project ki basic information aur instructions.

## How to Run

1. Install the required libraries.

pip install -r requirements.txt


2. Copy `.env.example` to `.env` and add your Groq API key from
   [Groq Console](https://console.groq.com/keys):

GROQ_API_KEY=your_api_key

`GROQ_MODEL` is optional; it defaults to `openai/gpt-oss-120b`.

3. Run the project.

streamlit run app.py

## How to Use

- Upload a PDF file or paste your text.
- Click on the **Summarize** button.
- The application will generate a short summary in 3 bullet points using Groq.

## About

I built this project to practice Python, Streamlit, API integration, and Prompt Engineering. It was also created as part of a Python & AI internship assignment.

## Author

**Sandeep Singh**