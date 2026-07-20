# AI Text Summarizer

This is a simple AI Text Summarizer project built using Python, Streamlit, and Google Gemini AI.

The application allows users to either paste text or upload a PDF file. It then generates a short summary in 3 bullet points using Gemini AI.

## Features

- Summarize long text
- Upload and summarize PDF files
- Google Gemini AI integration
- Character count
- Simple and user-friendly interface

## Technologies Used

- Python
- Streamlit
- Google Gemini AI
- PyPDF2
- python-dotenv

## Project Structure

- app.py = Main file jisme Streamlit UI aur application ka logic hai.

- utils/gemini.py = Gemini AI API ko handle karta hai aur summary generate karta hai.

- utils/pdf_reader.py = Uploaded PDF se text extract karta hai.

- requirements.txt = Project me use hone wali libraries ki list.

- .env = Gemini API Key store karne ke liye.

- .gitignore = Unnecessary files ko GitHub par upload hone se rokta hai.

- README.md = Project ki basic information aur instructions.

## How to Run

1. Install the required libraries.

pip install -r requirements.txt


2. Add your Gemini API key inside the .env file.

GEMINI_API_KEY=your_api_key

3. Run the project.

streamlit run app.py

## How to Use

- Upload a PDF file or paste your text.
- Click on the **Summarize** button.
- The application will generate a short summary in 3 bullet points.

## About

I built this project to practice Python, Streamlit, API integration, and Prompt Engineering. It was also created as part of a Python & AI internship assignment.

## Author

**Sandeep Singh**