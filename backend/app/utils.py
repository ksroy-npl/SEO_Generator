import pandas as pd

def load_products(file_path: str) -> list:
    ext = file_path.split('.')[-1].lower()
    if ext in ['xlsx', 'xls']:
        df = pd.read_excel(file_path)
    elif ext == 'csv':
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported product file format.")
    # Normalize columns for easier downstream use
    cols = [c.lower().replace(" ", "_") for c in df.columns]
    df.columns = cols
    # Return as dicts
    return df.to_dict(orient='records')
