import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_incident(alert_data, question=None):
    prompt = f"""
You are InsightGuard AI, a cybersecurity incident investigation assistant.

Analyze the following security alert.

SECURITY ALERT:
{alert_data}

USER QUESTION:
{question or "Explain why this alert is suspicious."}

Give a concise investigation report with:

1. Risk explanation
2. Evidence from the alert
3. Possible legitimate explanation
4. Recommended investigation steps

Only use information provided in the alert.
Do not invent facts.
Clearly distinguish evidence from assumptions.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text