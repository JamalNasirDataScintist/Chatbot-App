from google import genai
from config import GEMINI_API_KEY
from prompts import SYSTEM_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(question):

    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text