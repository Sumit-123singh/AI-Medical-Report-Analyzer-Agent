🏥 AI Medical Report Analyzer

Backend & AI System using FastAPI, OCR, and Multi-Agent LLM Architecture

AI Medical Report Analyzer is a backend-focused, production-style AI system designed to help both doctors and patients understand medical reports easily.
It processes medical reports (PDF/images), extracts text using OCR, analyzes the content using AI agents, explains results based on user role, supports multiple Indian languages, and generates audio output.

⚠️ This project intentionally focuses on backend engineering, AI system design, and real-world workflows. Frontend is minimal and Swagger UI is used for interaction.

🎯 Problem Statement

Medical reports are often:

Difficult for patients to understand

Time-consuming for doctors to interpret and explain

This system bridges that gap by:

Providing doctor-level technical insights

Providing patient-friendly explanations

Supporting regional languages

Offering audio explanations for accessibility

🧑‍⚕️ Two Explanation Modes (Core Feature)
🔹 Doctor Mode

Technical and clinical explanation

Uses medical terminology

Helps doctors quickly review reports

Suitable for professional understanding

🔹 Patient Mode

Simple, easy-to-understand language

Explains medical terms step-by-step

Designed for non-technical users

Improves patient awareness and clarity

👉 The same report is processed differently based on the selected mode.

🌍 Multilingual Support

Supported languages:

✅ English

✅ Hindi

✅ Marathi

✅ Tamil

This improves accessibility in Indian healthcare environments.
The translation logic is modular and can be extended easily.

🚀 Key Features

🔐 OAuth2 + JWT authentication

📄 Upload medical reports (PDF / Image)

🧠 Multi-Agent AI architecture

🧑‍⚕️ Doctor & Patient explanation modes

🌍 Multilingual medical explanations

🔊 Text-to-Speech audio generation

🗂️ User-specific report history

⚙️ Background task processing

🧱 Clean, modular FastAPI architecture

🧠 High-Level System Flow
Medical Report (PDF / Image)
        ↓
OCR Extraction
        ↓
Text Cleaning
        ↓
Medical Understanding Agent
        ↓
Mode Selection (Doctor / Patient)
        ↓
Explanation Agent
        ↓
Translation Agent
        ↓
Text-to-Speech Agent
        ↓
Database Storage + Audio File

📄 OCR (Optical Character Recognition)
Why OCR?

Medical reports are often scanned PDFs or images.
AI models cannot directly read images — OCR converts them into text.

OCR Tools Used

pytesseract → Text extraction

Pillow (PIL) → Image preprocessing

PDF reader → PDF text extraction

OpenCV (experiments) → Improve OCR accuracy

OCR Pipeline

Detect file type (PDF/Image)

Convert pages to images if needed

Extract raw text

Clean noisy OCR output

Pass clean text to AI agents

🧠 AI Architecture (Multi-Agent Design)

Each AI agent has one responsibility:

Medical Agent → Understands medical content

Explanation Agent → Simplifies medical language

Translation Agent → Converts language

Voice Agent → Generates audio output

This follows Single Responsibility Principle and keeps the system modular.

🧩 Service Layer (Important Design Choice)

AI logic is separated from API routes using a service layer.

Services:

llm_service.py → Central LLM interface

report_processor.py → End-to-end report pipeline

service_processor.py → Coordinates agents

translation_service.py → Language handling

tts_service.py → Audio generation

👉 This makes the system scalable, testable, and clean.

🦙 Ollama Server & LLaMA 3.2
What is Ollama?

Ollama is a local LLM server that runs large language models offline.

Why Ollama?

No paid API dependency

Full data privacy (important for medical data)

Faster local experimentation

Model Used

LLaMA 3.2 (latest)

Use Cases

Medical understanding

Explanation generation

Summarization

Translation prompts

🔊 Text-to-Speech (Audio Generation)

Uses gTTS (Google Text-to-Speech)

Converts final explanation into audio

Audio files stored per report

Helpful for:

Visually impaired users

Elderly patients

Audio-based understanding

Audio files are stored in the audio/ directory.

⚙️ Background Tasks (FastAPI)

Heavy operations like:

OCR

AI inference

Translation

Audio generation

are executed using FastAPI BackgroundTasks.

Benefits:

Faster API response

Non-blocking execution

Better scalability

Improved user experience

📁 Complete Project Structure

****ai-medical-report-agent/
│
├── app/
│   ├── __init__.py
│   │
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── deps.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── report.py
│   │   └── analysis.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── auth.py
│   │   └── report.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   ├── hashing.py
│   │   └── routes.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── medical_agent.py
│   │   ├── explain_agent.py
│   │   ├── translate_agent.py
│   │   └── voice_agent.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py
│   │   ├── report_processor.py
│   │   ├── service_processor.py
│   │   ├── translation_service.py
│   │   └── tts_service.py
│   │
│   ├── ocr/
│   │   ├── __init__.py
│   │   ├── pdf_reader.py
│   │   ├── image_reader.py
│   │   └── clean_text.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── report_routes.py
│   │   └── history_routes.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py
│   │   └── response_utils.py
│   │
│   ├── test_agent_run.py
│   ├── test_cv2.py
│   └── test_ocr.py
│
├── uploads/
├── audio/
│
├── requirements.txt
├── .env
└── README.md
****

1️⃣ Clone the Repository

Open your terminal and run:

git clone https://github.com/<your-username>/ai-medical-report-agent.git


Move into the project folder:

cd ai-medical-report-agent

2️⃣ Create a Virtual Environment (Recommended)
On Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install Project Dependencies
pip install -r requirements.txt

4️⃣ Install System Dependencies (Important)
🧾 Tesseract OCR (Required)
Windows

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Install and note the path (example):

C:\Program Files\Tesseract-OCR\tesseract.exe


Add it to System PATH

🧠 Ollama (LLM Server)

Download Ollama from:
https://ollama.com/download

Install and start Ollama

Pull the model:

ollama pull llama3.2


Verify Ollama is running:

ollama list

5️⃣ Create .env File

In the project root, create a .env file:

DATABASE_URL=sqlite:///./medical.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

6️⃣ Initialize the Database

If required:

python app/db/init_db.py


This creates database tables.

7️⃣ Start the FastAPI Server
uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000

8️⃣ Open Swagger UI (Main Interface)

Open your browser:

http://127.0.0.1:8000/docs


## 👤 Author

**Sumit Singh**  
Backend & AI Engineer  

Passionate about building scalable backend systems and AI-powered applications using FastAPI, OCR pipelines, LLMs, and clean architecture principles.
