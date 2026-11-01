import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class GroqSummaryError(Exception):
    """Raised when Groq does not return a usable summary."""


def generate_summary(user_text: str) -> str:
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("GROK_API_KEY")
    if not api_key or not api_key.strip():
        raise ValueError("Set GROQ_API_KEY in your .env file before summarizing.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL") or os.getenv(
            "GROK_MODEL", "openai/gpt-oss-120b"
        ),
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional AI Text Summarizer. Summarize the "
                    "user's text into exactly 3 concise bullet points. Preserve "
                    "the original meaning, use simple and clear English, and "
                    "do not add information. Return only the bullet points, "
                    "without headings, introductions, or conclusions."
                ),
            },
            {"role": "user", "content": user_text},
        ],
    )

    if not response.choices:
        raise GroqSummaryError("Groq returned no summary.")

    summary = response.choices[0].message.content
    if not summary or not summary.strip():
        raise GroqSummaryError("Groq returned an empty summary.")

    return summary.strip()


def get_api_error_message(error: Exception) -> str:
    response = getattr(error, "response", None)
    if response is not None:
        try:
            payload = response.json()
        except ValueError:
            pass
        else:
            if isinstance(payload, dict):
                message = payload.get("error")
                if isinstance(message, str):
                    return message

    return str(error)