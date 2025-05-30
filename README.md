# SEO_Generator

# ✨ SEO Product Description Generator

A modern, AI-powered tool for generating SEO-optimized product titles and descriptions for fashion e-commerce, inspired by luxury Shopify themes.  
Built with FastAPI (Python) for the backend and React (Material UI) for the frontend.  
Integrates Google Gemini for high-quality, keyword-rich, occasion-aware product copywriting.

---

## 🚀 Features

- **AI-generated SEO titles and descriptions** using Google Gemini API
- **Occasion-aware:** Detects special occasions (like “homecoming”, “bridal shower”, etc.) and incorporates them into the output
- **Keyword-rich:** Uses a curated list of high-value SEO keywords for fashion
- **Modern UI:** Clean, elegant React frontend styled after luxury e-commerce themes
- **Easy to use:** Simple form, instant results, copy-paste ready
- **Logs all activity:** Stores each input and output in a `.txt` log for review

---

## 🗂️ Project Structure

```
product-description-generator/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI entrypoint
│   │   ├── seo_generator.py      # Prompt logic, keyword/occasion handling
│   │   ├── gemini_client.py      # Gemini API client
│   │   ├── config.py             # Settings loader
│   │   └── product_seo_log.txt   # (auto-created) Log file
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── src/
│   │   └── App.js                # Main React app
│   ├── public/
│   │   └── index.html            # Includes Google Fonts
│   └── package.json              # Frontend dependencies
└── README.md
```

---

## ⚡ Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/your-username/product-description-generator.git
cd product-description-generator
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate # On Mac/Linux

pip install -r requirements.txt
```

#### Configure Gemini API Key

- Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- Create a `.env` file in `backend/app/` with:
  ```
  GEMINI_API_KEY=your-key-here
  PROJECT_NAME=SEO Product Description Generator
  ALLOWED_ORIGINS=*
  ```

### 3. Start the backend

```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be running at: [http://localhost:8000](http://localhost:8000)

---

### 4. Set up the frontend

```bash
cd ../frontend
npm install
```

### 5. Start the frontend

```bash
npm start
```

The app will open at: [http://localhost:3000](http://localhost:3000)

---

## 📝 Usage

1. Fill in the **Handle**, **Title**, and **Body** fields in the form.
2. Optionally, add a **Brand Tone** (e.g., “luxury”, “fun”, “minimal”).
3. Click **Generate SEO Description**.
4. The app will display:
    - Optimized Title
    - Optimized Body (plain text)
    - Keywords Used
5. All requests and results are logged in `backend/app/product_seo_log.txt`.

---

## 🎯 How Occasion Detection Works

- The backend checks your input for occasion keywords (like "homecoming dresses", "bridal shower dress", etc.).
- If an occasion is detected, the AI is instructed to include it in both the title and body.
- If not, a general SEO description is generated.

---

## 🛠️ Customization

- **Add more keywords:** Edit `keywords_list` in `seo_generator.py`.
- **Add/modify occasions:** Edit `occasion_keywords` in `seo_generator.py`.
- **Change prompt style:** Edit the `build_prompt` function.
- **Change log location:** Edit the `log_path` in `main.py`.

---

## 🧩 Dependencies

### Backend (`backend/requirements.txt`)

- fastapi
- uvicorn
- pandas
- python-dotenv
- google-generativeai
- openpyxl

### Frontend (`frontend/package.json`)

- react
- react-dom
- @mui/material
- @emotion/react
- @emotion/styled
- axios

---

## 💡 Tips

- For best results, provide clear product titles and bodies.
- The tool works with only handle, title, and body—no need for product type or category.
- If you want HTML output, adjust the prompt in `seo_generator.py`.

---

## 📝 License

MIT License

---

## 🙋 FAQ

**Q: Why is the output blank?**  
A: Check your Gemini API quota, and ensure the backend is running with the correct API key.

**Q: How do I add more SEO keywords?**  
A: Edit the `keywords_list` in `seo_generator.py`.

**Q: Can I deploy this to production?**  
A: Yes! You can deploy the FastAPI backend and React frontend to your preferred cloud provider.

---

## 👑 Credits

- Built by Kritanta Sasan Roy
- Powered by [Google Gemini](https://aistudio.google.com/), FastAPI, and React

---

**Enjoy effortless, AI-powered, SEO-optimized product copywriting!**

---
