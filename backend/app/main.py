from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .seo_generator import process_product
import os
import datetime

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .gemini_client import configure_gemini
configure_gemini()

@app.post("/generate-seo")
async def generate_seo(
    handle: str = Form(...),
    title: str = Form(...),
    body: str = Form(...),
    brand_tone: str = Form("")
):
    product = {
        "handle": handle,
        "title": title,
        "body": body
    }
    result = process_product(product, brand_tone)

    # --- Store input and output in a txt file ---
    log_path = os.path.join(os.path.dirname(__file__), "product_seo_log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Timestamp: {datetime.datetime.now()}\n")
        f.write("INPUT:\n")
        for k, v in product.items():
            f.write(f"  {k}: {v}\n")
        f.write(f"  brand_tone: {brand_tone}\n")
        f.write("OUTPUT:\n")
        f.write(f"  Optimized Title: {result['optimized_title']}\n")
        f.write(f"  Optimized Body: {result['optimized_body']}\n")
        f.write(f"  Keywords Used: {result['keywords_used']}\n")
        f.write(f"{'='*60}\n")

    return {"status": "success", "result": result}

@app.get("/")
def root():
    return {"message": "SEO Product Description Generator API is running."}
