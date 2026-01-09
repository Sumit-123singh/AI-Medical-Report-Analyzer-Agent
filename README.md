🩺 AI Medical Report Analyzer
Built for Doctors. Designed for Patients.

AI Medical Report Analyzer is a backend-focused, production-style AI system that transforms complex medical reports into clear, understandable insights.
It supports doctor-level technical explanations, patient-friendly summaries, regional languages, and audio output, making medical information accessible to everyone.

⚠️ This project intentionally focuses on backend engineering, AI system design, and real-world healthcare workflows.
Frontend is minimal — Swagger UI is used as the primary interface.

🎯 Problem Statement

Medical reports are often:

Hard for patients to understand

Time-consuming for doctors to explain

Written in complex medical terminology

Delivered as scanned PDFs or images

This project solves these problems by combining OCR, AI agents, language translation, and audio generation into a single backend system.

🧑‍⚕️ Two Explanation Modes (Core Feature)
🔹 Doctor Mode

Technical and clinical explanation

Uses proper medical terminology

Helps doctors quickly review reports

Suitable for diagnosis and professional use

🔹 Patient Mode

Simple, human-friendly language

Explains medical terms step-by-step

Designed for non-technical users

Helps patients understand their health clearly

👉 The same medical report is processed differently based on the selected mode.

🌍 Multilingual Support

The system supports the following languages:

✅ English

✅ Hindi

✅ Marathi

✅ Tamil

This makes the system suitable for Indian healthcare environments and improves accessibility for non-English users.

🚀 Key Features

🔐 OAuth2 + JWT authentication

📄 Upload medical reports (PDF / Image)

🧠 Multi-Agent AI architecture

🧑‍⚕️ Doctor & Patient explanation modes

🌍 Multilingual medical explanations

🔊 Text-to-Speech audio generation

🗂️ User-specific report history

⚙️ Background task processing

🧱 Clean, modular FastAPI backend design

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
AI models cannot read images directly, so OCR converts them into text.

OCR Tools Used

pytesseract → Extracts text from images

Pillow (PIL) → Image preprocessing

PDF reader → Extracts text from PDF files

OpenCV (experiments) → Improves OCR accuracy

OCR Pipeline

Detect file type (PDF or image)

Convert pages to images if needed

Extract raw text

Clean noisy OCR output

Pass clean text to AI agents

🧠 AI Architecture (Multi-Agent Design)

This project follows a multi-agent AI architecture, where each agent has one clear responsibility.

AI Agents

Medical Agent → Understands medical content

Explanation Agent → Simplifies information

Translation Agent → Converts language

Voice Agent → Generates audio output

This design follows the Single Responsibility Principle and keeps the system modular and extensible.

🦙 Ollama Server & LLaMA 3.2
What is Ollama?

Ollama is a local LLM server that allows running large language models offline.

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

Audio files are stored per report

Helpful for:

Visually impaired users

Elderly patients

Audio-based understanding

Audio files are saved in the audio/ directory.

⚙️ Background Tasks (FastAPI)

Heavy operations such as:

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


📁 Project Structure

ai-medical-report-agent/
│
├── app/
│   ├── __init__.py
│   │
│   ├── main.py                     # FastAPI app entry point
│   │
│   ├── core/                       # App-wide settings & security
│   │   ├── __init__.py
│   │   ├── config.py               # Environment variables
│   │   ├── security.py             # JWT, OAuth2, security utils
│   │   └── deps.py                 # Common dependencies
│   │
│   ├── db/                         # Database setup
│   │   ├── __init__.py
│   │   ├── base.py                 # SQLAlchemy Base
│   │   ├── session.py              # DB session management
│   │   └── init_db.py              # Table creation logic
│   │
│   ├── models/                     # ORM models
│   │   ├── __init__.py
│   │   ├── user.py                 # User table
│   │   ├── report.py               # Medical reports table
│   │   └── analysis.py             # AI analysis results
│   │
│   ├── schemas/                    # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── auth.py
│   │   └── report.py
│   │
│   ├── auth/                       # Authentication logic
│   │   ├── __init__.py
│   │   ├── jwt.py                  # JWT create/verify
│   │   ├── hashing.py              # Password hashing (bcrypt)
│   │   └── routes.py               # Register/Login APIs
│   │
│   ├── agents/                     # AI Agents
│   │   ├── __init__.py
│   │   ├── medical_agent.py        # Medical understanding agent
│   │   ├── explain_agent.py        # Simplified explanation agent
│   │   ├── translate_agent.py      # Multilingual translation agent
│   │   └── voice_agent.py          # Text-to-speech agent
│   │
│   ├── services/                   # Service layer (AI orchestration)
│   │   ├── __init__.py
│   │   ├── llm_service.py          # Central LLM abstraction
│   │   ├── report_processor.py     # End-to-end report pipeline
│   │   ├── service_processor.py    # Coordinates multiple agents
│   │   ├── translation_service.py  # Translation logic
│   │   └── tts_service.py          # Text-to-speech service
│   │
│   ├── ocr/                        # OCR & preprocessing
│   │   ├── __init__.py
│   │   ├── pdf_reader.py           # PDF text extraction
│   │   ├── image_reader.py         # Image OCR
│   │   └── clean_text.py           # OCR text cleaning
│   │
│   ├── api/                        # API routes
│   │   ├── __init__.py
│   │   ├── report_routes.py        # Upload & analyze report
│   │   └── history_routes.py       # User report history
│   │
│   ├── utils/                      # Helper utilities
│   │   ├── __init__.py
│   │   ├── file_utils.py           # File handling helpers
│   │   └── response_utils.py       # Common API responses
│   │
│   ├── test_agent_run.py           # Agent pipeline testing (dev only)
│   ├── test_cv2.py                 # OpenCV experimentation
│   └── test_ocr.py                 # OCR testing & debugging
│
├── uploads/                        # Uploaded medical reports
├── audio/                          # Generated TTS audio files
│
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables
└── README.md                       # Project documentation


▶️ How to Run the Project (After Clone)
git clone 
cd ai-medical-report-agent

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs


👤 Author

Sumit Singh
Backend & AI Engineer

Focused on building scalable backend systems and AI-powered applications using FastAPI, OCR pipelines, LLMs, and clean architecture principles.
