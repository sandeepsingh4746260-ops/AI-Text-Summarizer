import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Generate Summary Function
def generate_summary(user_text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a professional AI Text Summarizer.

Summarize the following text into exactly 3 concise bullet points.

Instructions:
- Preserve the original meaning.
- Use simple and clear English.
- Do not add any new information.
- Keep each bullet point short.
- Return only bullet points.
- Do not write headings, introductions or conclusions.

Text:
{user_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {e}"