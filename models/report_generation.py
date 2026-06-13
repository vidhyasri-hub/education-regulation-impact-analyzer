import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-flash-latest"
)

#for model in genai.list_models():
 #   print("~supported model names~",model.name)

def generate_policy_report(
    document_text,
    topic_result,
    chronology_result,
    impact_result,
    risk_result
):
    


    prompt = f"""
You are an AI Education Policy Analyst.

Analyze the following education regulation document.

==================================================
DOCUMENT ANALYSIS RESULTS
==================================================

TOPIC CLASSIFICATION:
{topic_result}

CHRONOLOGY INFORMATION:
{chronology_result}

STAKEHOLDER IMPACTS:
{impact_result}

RISK DETECTION:
{risk_result}

==================================================
REGULATION TEXT
==================================================

{document_text[:12000]}

==================================================
TASK
==================================================

Generate a structured policy intelligence report.

Your response must contain:

1. EASY SUMMARY
- Write a simple 10-20 line explanation.
- Explain the regulation in plain English.
- Make it understandable for students and faculty.

2. STAKEHOLDER IMPACT REPORT
Explain:
- Which stakeholders benefit
- Which stakeholders may face challenges
- New academic or institutional opportunities

Stakeholders include:
- students
- faculty
- institutions
- administrators
- accreditation/compliance teams

3. CHRONOLOGY & POLICY CONTEXT
Explain:
- possible amendments
- predecessor circulars
- policy evolution signals

4. IMPACT ASSESSMENT

Provide:
- Short-term impact (0-1 year)
- Medium-term impact (1-5 years)
- Long-term impact (>5 years)

5. POSITIVES
Provide bullet points.

6. NEGATIVES / RISKS
Provide bullet points.

7. INSTITUTIONAL READINESS CHALLENGES
Explain possible:
- compliance burden
- accreditation challenges
- implementation difficulties

Use clear headings.
Keep explanations simple and practical.
"""

    response = model.generate_content(prompt)

    return response.text