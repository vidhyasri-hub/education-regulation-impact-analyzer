import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-flash-latest")


def summarize_document(text):

    prompt = f"""
    Analyze this education regulation.

    Provide:

    1. Simple summary
    2. Stakeholders affected
    3. Short-term impact
    4. Medium-term impact
    5. Long-term impact
    6. Risks
    7. Opportunities

    Regulation Text:
    {text[:12000]}
    """

    response = model.generate_content(prompt)

    return response.text