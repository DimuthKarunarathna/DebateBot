import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_argument(topic, stance):
    prompt = f"""
    Debate the topic: "{topic}". Take the {stance} side.
    Give me 3 persuasive arguments, each with reasoning and examples.
    Format them with bullet points.
    """
    response = model.generate_content(prompt)
    return response.text