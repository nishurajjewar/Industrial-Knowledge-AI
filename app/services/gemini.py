import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

# Read API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text