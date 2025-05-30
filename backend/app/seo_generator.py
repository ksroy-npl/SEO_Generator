import re
import json
from typing import Dict
from .gemini_client import generate_description

# Hardcoded SEO keywords list
keywords_list = [
    'dress for the graduation', 'homecoming dresses', 'bridal shower dresses', 'white heels',
    'black with dress', 'grad dresses', 'black wedding guest dress', 'black prom dress',
    'halter dress', 'christmas dress', 'pink maxi dress', 'lavender dress', 'light blue dress',
    'burgundy dress', 'navy blue dress', 'denim dress', 'short white dress', 'black bridesmaid dresses',
    'hot pink dress', 'babydoll dress', 'white jumpsuit', 'black dresses for women', 'bridal shower dress',
    'black midi dress', 'dresses and white', 'nude heels', 'long sleeve white dress', 'white long sleeve dress',
    'black prom dresses', 'pleated dress', 'baby doll dress', 'emerald green dress', 'black cocktail dress',
    'white mini dress', 'sparkly dress', 'heel shoes white', 'black jumpsuit', 'new years eve outfit',
    'white midi dress', 'black formal dresses', 'black maxi dress', 'blue heels', 'sequin jumpsuit',
    'red cocktail dress', 'silver heels', 'baby shower dresses', 'white top', 'country concert outfit',
    'white sweater', 'black lace dress', 'white lace dress', 'navy dress', 'baby blue dress', 'sequin mini dress',
    'ruffle dress', 'orange dress', 'summer outfits', 'burnt orange dress', 'black formal dress',
    'black strappy heels', 'plaid dress', 'red cocktail dress', 'beach wedding dresses',
    'sage green bridesmaid dresses', 'black with dress', 'pink heels', 'blue dresses for women',
    'gold heel heels', 'dress for black', 'fit and flare dress', 'gingham dress', 'womens swim shorts',
    'and crop top', 'white button up shirt', 'dress for black', 'black dresses black dresses', 'red heels',
    'dress for the graduation', 'silver dress', 'sequin dress', 'lace top', 'white kitten heels',
    'dress for prom black', 'brown dress', 'red mini dress', 'babydoll tops', 'yellow dress',
    'brown trousers pants', 'blue floral dress', 'bubble dress', 'birthday outfits', 'dresses and white',
    'modest wedding dresses', 'blue dress', 'vestidos de fiesta', 'off the shoulder dress', 'champagne dress',
    'pink dresses for women', 'navy blue dress', 'mx dresses', 'black top', 'long sleeve dress',
    'purple prom dress', 'black long sleeve dress', 'gold dress', 'peplum', 'white corset top', 'lilac dress',
    'pink dresses', 'boho dresses', 'red top', 'black corset top', 'lace dress', 'black tie wedding guest dress',
    'peplum top', 'white crop top', 'heel shoes white', 'one shoulder dress', 'prom black gown', 'vestidos',
    'bustier', 'fringe dress', 'winter formal dresses', 'black bikini', 'white mini dress', 'black mini skirt',
    'rehearsal dinner dress', 'red sweater', 'wedding shoes', 'bustier', 'babydoll top', 'old hollywood outfits',
    'white cowboy boots', 'black tie dresses', 'long sleeve mini dress', 'sequin top', 'old hollywood dresses',
    'shop kitten heels', 'olive green dress', 'crochet dress', 'short white dress', 'yellow dress dress',
    'green sweater', 'tulle dress', 'pink floral dress', 'overall dress', 'sexy black dress', 'purple dresses',
    'mardi gras outfits', 'sequin jumpsuit', 'purple dresses for women', 'old money style', 'denim romper',
    'red prom dress', 'pink sweater', 'long sleeve wedding dresses', 'dippin daisy', 'holiday dresses',
    'micro shorts', "women's tops on sale", 'concert outfits', 'gold prom dress', 'black platform heels',
    'country concert outfit', 'black wedding dresses', 'mesh top', 'strappy heels', 'white maxi dress',
    'brown boots', 'quinceanera dresses near me', 'dress for the graduation', 'hello molly dresses',
    'black prom dresses', 'white mini skirt', 'white corset', 'blue floral dress', 'mexican for women',
    'kentucky derby outfits', 'gold shoes', 'turtleneck', 'shoes for black', 'reebok club c', 'homecoming dresses',
    'mermaid wedding dress', 'lace dress', 'sunlight dresses', 'mary jane heels', 'grad dresses',
    'ankle boots for women', 'black lace dress', 'pearl heels', 'vervet jeans', 'black sweater', 'boat neck top',
    'black boots', 'red mini dress', 'strapless dress', 'slate blue', 'heeled boots', 'long cardigan long',
    'olive green dress', 'mini jean skirt'
]

# List of occasion keywords (subset for matching)
occasion_keywords = [
    'dress for the graduation', 'homecoming dresses', 'bridal shower dresses', 'bridal shower dress',
    'grad dresses', 'black wedding guest dress', 'black prom dress', 'black prom dresses',
    'new years eve outfit', 'baby shower dresses', 'birthday outfits', 'modest wedding dresses',
    'beach wedding dresses', 'sage green bridesmaid dresses', 'wedding shoes', 'rehearsal dinner dress',
    'old hollywood outfits', 'old hollywood dresses', 'winter formal dresses', 'quinceanera dresses near me',
    'kentucky derby outfits', 'mermaid wedding dress', 'holiday dresses', 'mardi gras outfits',
    'concert outfits', 'gold prom dress', 'country concert outfit', 'black wedding dresses',
    'black tie wedding guest dress', 'black tie dresses', 'prom black gown', 'red prom dress'
]

def find_occasion(input_text: str) -> str:
    """Returns the first matching occasion keyword found in the input text, or '' if none."""
    input_text_lower = input_text.lower()
    for occasion in occasion_keywords:
        if occasion in input_text_lower:
            return occasion
    return ""

def clean_json_response(raw_result: str) -> str:
    """
    Removes Markdown code block markers (``````) from Gemini output.
    """
    lines = raw_result.strip().splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()

def build_prompt(product: dict, brand_tone: str = "") -> str:
    # Combine all input fields for occasion detection
    combined_input = " ".join([
        product.get('handle', ''),
        product.get('title', ''),
        product.get('body', ''),
        product.get('type', ''),
        product.get('category', '')
    ])
    occasion = find_occasion(combined_input)

    # If an occasion is matched, add an instruction to include it in the title/body
    occasion_instruction = ""
    if occasion:
        occasion_instruction = (
            f"\nIMPORTANT: This product is for the occasion: '{occasion}'. "
            "Include the occasion name in both the optimized title and body in a natural, prominent way."
        )

    return f"""
You are an expert SEO content creator for a fashion e-commerce site.

Here is a list of high-value SEO keywords:
{', '.join(keywords_list)}

Given the following product details:
- Handle: {product.get('handle', '')}
- Title: {product.get('title', '')}
- Body: {product.get('body', '')}
- Product Category: {product.get('category', '')}
- Type: {product.get('type', '')}
{occasion_instruction}

Your tasks:
1. Analyze the keyword list and select the most relevant, high-impact SEO keywords for this product.
2. Rewrite the product Title for maximum SEO impact:
    - Use 1-2 of the best keywords
    - Make it highly relevant and compelling
    - Limit to a maximum of 7 words
    {"- Include the occasion name in the title." if occasion else ""}
3. Rewrite the product Body/Description:
    - Make it compelling and SEO-optimized
    - Naturally use the best-matching keywords
    - Keep it under 120 words
    - Ensure it reads naturally for shoppers
    {"- Include the occasion name in the body." if occasion else ""}
4. Output your answer as a JSON object with these fields:
   {{
     "optimized_title": "...",
     "optimized_body": "...",
     "keywords_used": ["...", "...", ...]
   }}
Only output the JSON. Do not add explanations.
"""

def process_product(product: dict, brand_tone: str) -> dict:
    prompt = build_prompt(product, brand_tone)
    raw_result = generate_description(prompt)
    cleaned = clean_json_response(raw_result)
    try:
        result = json.loads(cleaned)
        return {
            "optimized_title": result.get("optimized_title", ""),
            "optimized_body": result.get("optimized_body", ""),
            "keywords_used": ", ".join(result.get("keywords_used", []))
        }
    except Exception as e:
        print("JSON parsing error:", e)
        print("Raw Gemini output:", raw_result)
        print("Cleaned Gemini output:", cleaned)
        return {
            "optimized_title": "",
            "optimized_body": "",
            "keywords_used": ""
        }
