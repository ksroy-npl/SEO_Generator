import google.generativeai as genai
from .config import settings

def configure_gemini():
    genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_description(prompt: str) -> str:
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    try:
        response = model.generate_content(prompt)
        print("Gemini response:", response)
        return response.text.strip() if response.text else ""
    except Exception as e:
        print("Gemini API Exception:", e)
        return ""
