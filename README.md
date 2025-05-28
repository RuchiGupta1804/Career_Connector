# 🤖 Career Connector

**Optimize your resume with AI.**  
Career Connector is a smart web-based resume checker built using Streamlit and powered by Google's Gemini AI.
It helps you analyze your resume against job descriptions, offering deep insights like keyword relevance, grammar issues— all with one click.

---

## 🚀 Features

- 📄 Upload your resume (PDF format)  
- 📝 Paste any job description  
- 💡 Get an ATS-style match percentage  
- 🔍 Find missing keywords and skill gaps  
- ✍️ Spot grammar and spelling issues  
- 🧠 Improve work experience phrasing  

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – for the interactive website  
- [Google Gemini API](https://ai.google.dev/) – for intelligent content generation  
- [PyPDF2](https://pypi.org/project/PyPDF2/) – for extracting text from resumes  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – to securely manage API keys

---

## 💻 How to Run the Website Locally

1. **Clone the repository**
```bash
  pip install -r requirements.txt
```
3. **Launch the Streamlit website**
```bash
  streamlit run main.py
```

---

## 🔐 API Key Notice
You'll need a Gemini API key from **Google Cloud Console**.
To create one:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Generative Language API** in the API Library
4. Navigate to **APIs & Services > Credentials**
5. Click **“Create Credentials” → API Key**
6. Copy and save the key securely

**Set up your environment**
Create a .env file and add your Gemini API key:
```bash
  GEMINI_API_KEY=your_gemini_api_key_here
```
---

## 📁 Project Structure
```bash
├── main.py # Streamlit website script
├── .env # Environment file for API key
└── README.md # Project documentation
```

---

## 📌 Example Workflow

1. Upload your resume as a PDF
2. Paste the job description in the text area
3. Click Submit
4. Get:  
   - ✅ Match percentage  
   - 📉 Missing keywords  
   - ✍️ Grammar/spelling feedback  
   - 💼 Suggested experience updates

---
