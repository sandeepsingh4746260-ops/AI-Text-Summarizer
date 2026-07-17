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

AI_Text_Summarizer/
│
├── utils/
│   ├── gemini.py
│   └── pdf_reader.py
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

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