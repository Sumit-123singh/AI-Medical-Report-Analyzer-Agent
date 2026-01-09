🩺 AI Medical Report Analyzer
Built for Doctors. Designed for Patients.

A backend-focused, production-style AI system that transforms complex medical reports into clear, actionable insights.

This system supports:

🧑‍⚕️ Doctor-level technical explanations

🧍 Patient-friendly summaries

🌍 Regional Indian languages

🔊 Audio output (Text-to-Speech)

⚠️ Note:
This project intentionally focuses on backend engineering, AI system design, and real healthcare workflows.
The frontend is minimal — Swagger UI is the primary interface.

🎯 Problem Statement

Medical reports today are often:

❌ Hard for patients to understand

⏱️ Time-consuming for doctors to explain

📄 Filled with complex medical terminology

🖨️ Delivered as scanned PDFs or images

✅ Solution

This system combines:

OCR

AI agents

Language translation

Audio generation

into one clean, scalable backend pipeline.

🧑‍⚕️ Core Feature — Two Explanation Modes
🔹 Doctor Mode

Technical & clinical explanations

Uses proper medical terminology

Helps doctors review reports faster

Suitable for diagnosis & professional use

🔹 Patient Mode

Simple, human-friendly language

Medical terms explained step-by-step

Designed for non-technical users

Improves patient understanding

👉 The same report is processed differently based on the selected mode.

🌍 Multilingual Support (India-Focused)

Supported languages:

✅ English

✅ Hindi

✅ Marathi

✅ Tamil

This makes the system suitable for Indian healthcare environments and improves accessibility for non-English users.

🚀 Key Features

🔐 OAuth2 + JWT Authentication

📄 Upload Medical Reports (PDF / Image)

🧠 Multi-Agent AI Architecture

🧑‍⚕️ Doctor & Patient Explanation Modes

🌍 Multilingual Medical Explanations

🔊 Text-to-Speech Audio Output

🗂️ User-Specific Report History

⚙️ Background Task Processing

🧱 Clean, Modular FastAPI Backend

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
AI models cannot read images directly — OCR converts them into text.

OCR Tools Used

pytesseract → Image text extraction

Pillow (PIL) → Image preprocessing

PDF reader → PDF text extraction

OpenCV → OCR accuracy experiments

OCR Pipeline

Detect file type (PDF / Image)

Convert PDF pages to images (if needed)

Extract raw text

Clean noisy OCR output

Send clean text to AI agents

🧠 AI Architecture — Multi-Agent Design

Each agent has one clear responsibility (Single Responsibility Principle).

AI Agents

Medical Agent → Understands medical content

Explanation Agent → Simplifies & structures output

Translation Agent → Converts language

Voice Agent → Generates audio

✅ Modular
✅ Extensible
✅ Easy to maintain

🦙 Ollama Server & LLaMA 3.2
What is Ollama?

Ollama is a local LLM server that runs large language models offline.

Why Ollama?

🔒 Full data privacy (critical for medical data)

💸 No paid API dependency

⚡ Faster local experimentation

Model Used

LLaMA 3.2

Use Cases

Medical understanding

Explanation generation

Summarization

Translation prompts

🔊 Text-to-Speech (Audio Generation)

Uses gTTS (Google Text-to-Speech)

Converts final explanation into audio

Audio stored per report

Helpful For:

👁️ Visually impaired users

👵 Elderly patients

🎧 Audio-based understanding

Audio files are stored in the audio/ directory.

⚙️ Background Tasks (FastAPI)

Heavy operations like:

OCR processing

AI inference

Translation

Audio generation

are executed using FastAPI BackgroundTasks.

Benefits

Faster API response

Non-blocking execution

Better scalability

Improved user experience

📁 Project Structure (Clean & Explained)
ai-medical-report-agent/
│
├── app/                         # Main application package
│   ├── __init__.py
│   ├── main.py                  # FastAPI app entry point
│
│   ├── core/                    # App-wide config & security
│   │   ├── config.py            # Environment variables
│   │   ├── security.py          # JWT, OAuth2 utilities
│   │   └── deps.py              # Shared dependencies
│
│   ├── db/                      # Database setup
│   │   ├── base.py              # SQLAlchemy Base
│   │   ├── session.py           # DB session management
│   │   └── init_db.py           # Table creation logic
│
│   ├── models/                  # ORM models
│   │   ├── user.py              # User table
│   │   ├── report.py            # Medical reports
│   │   └── analysis.py          # AI analysis results
│
│   ├── schemas/                 # Pydantic schemas
│   │   ├── user.py
│   │   ├── auth.py
│   │   └── report.py
│
│   ├── auth/                    # Authentication logic
│   │   ├── jwt.py               # JWT create/verify
│   │   ├── hashing.py           # Password hashing
│   │   └── routes.py            # Register/Login APIs
│
│   ├── agents/                  # AI agents (single responsibility)
│   │   ├── medical_agent.py
│   │   ├── explain_agent.py
│   │   ├── translate_agent.py
│   │   └── voice_agent.py
│
│   ├── services/                # Business logic orchestration
│   │   ├── llm_service.py
│   │   ├── report_processor.py
│   │   ├── translation_service.py
│   │   └── tts_service.py
│
│   ├── ocr/                     # OCR & preprocessing
│   │   ├── pdf_reader.py
│   │   ├── image_reader.py
│   │   └── clean_text.py
│
│   ├── api/                     # API routes
│   │   ├── report_routes.py
│   │   └── history_routes.py
│
│   └── utils/                   # Helper utilities
│       ├── file_utils.py
│       └── response_utils.py
│
├── uploads/                     # Uploaded medical reports
├── audio/                       # Generated audio files
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
└── README.md                    # Project documentation

💡 Why This Structure?

Clear separation of concerns

Scales well in production

Easy onboarding for new developers

Matches real-world backend architecture

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone 
cd ai-medical-report-agent

2️⃣ Create Virtual Environment
python -m venv venv


Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Server
uvicorn app.main:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

👤 Author
Sumit Singh

Backend & AI Engineer

Focused on building scalable backend systems and AI-powered healthcare applications using:
