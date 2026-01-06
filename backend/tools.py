# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:

    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist.

Respond with:
- Emotional attunement
- Gentle normalization
- One practical suggestion OR reflection

Rules:
- Single paragraph only
- 3–4 sentences maximum
- Never exceed 100 tokens
- Ask at most ONE open-ended question
- End immediately after the question
- Be concise, calm, and human

Avoid labels, brackets, or clinical jargon.
"""

    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 120,
                'temperature': 0.6,
                'top_p': 0.85,
                'stop': ['\n\n']
            }
        )
        return response['message']['content'].strip()

    except Exception as e:
        return (
            "I'm having technical difficulties, but I want you to know "
            "your feelings matter. Please try again shortly."
        )


# Step2: Setup Twilio calling API tool
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        to=EMERGENCY_CONTACT,
        from_=TWILIO_FROM_NUMBER,
        url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
    )

# Step3: Setup Location tool

