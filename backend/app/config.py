import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    PROJECT_NAME: str = "SEO Product Description Generator"
    ALLOWED_ORIGINS = ["http://localhost:3000", "*"]
    OUTPUT_DIR = r"C:\Users\mithu\OneDrive\Desktop\nexus point luxe stuffs\desc output"

settings = Settings()
