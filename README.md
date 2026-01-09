🩺 AI Medical Report Analyzer

Built for Doctors. Designed for Patients.

FastAPI · OCR · Multi-Agent AI · Ollama · Text-to-Speech

A backend-focused, production-style AI system that converts complex medical reports (PDFs & images) into clear, multilingual, human-understandable medical explanations for both doctors and patients.

This system bridges the gap between raw medical reports and real-world understanding.

🔹 Features

🚀 Medical Report Understanding – Extracts and understands clinical data from scanned PDFs and images
🧠 Multi-Agent AI System – Separate agents for medical reasoning, explanation, translation, and voice
🧑‍⚕️ Doctor Mode – Technical, clinical, professional medical interpretation
🧍 Patient Mode – Simple, easy-to-understand health explanations
🌍 Multilingual Support – English, Hindi, Marathi, Tamil
🔊 Audio Output – Converts explanations into speech using Text-to-Speech
🔐 Secure System – OAuth2 + JWT authentication
🗂 User History – Stores report results and audio files per user
⚙️ Background Processing – Heavy AI & OCR tasks run asynchronously
☁️ Deployment Ready – Works with cloud and local LLM servers

🔹 Problem Statement

Medical reports today are:

❌ Hard for patients to understand
⏱ Time-consuming for doctors to explain
📄 Written in complex medical language
🖨 Often provided as scanned PDFs or images

This leads to confusion, delays, and misinterpretation.

🔹 Solution

This system combines:

OCR (Optical Character Recognition)

AI medical reasoning

Language translation

Audio generation

into one automated backend pipeline that converts raw medical reports into clear, multilingual, spoken explanations.

🔹 Two Explanation Modes
🧑‍⚕️ Doctor Mode

Clinical & technical explanation

Uses correct medical terminology

Designed for diagnosis & review

Helps doctors save time

🧍 Patient Mode

Simple, friendly language

Medical terms explained step-by-step

Designed for non-technical users

Improves patient understanding

➡️ The same report is processed differently based on the selected mode.

🔹 Multilingual Support

Supported languages:

English

Hindi

Marathi

Tamil

This makes the system suitable for Indian healthcare environments and non-English speakers.



🔹 OCR System

Medical reports are often scanned PDFs or images.
AI cannot read images directly — OCR converts them into text.

Tools Used

pytesseract – image text extraction

Pillow – image preprocessing

PDF reader – PDF text extraction

OpenCV – OCR accuracy improvement

OCR Pipeline

Detect PDF or image

Convert pages to images (if needed)

Extract raw text

Clean OCR noise

Send to AI agents

🔹 AI Architecture

The system uses a Multi-Agent AI Design.

Agent	Role
Medical Agent	Understands medical content
Explanation Agent	Structures and simplifies output
Translation Agent	Converts to regional languages
Voice Agent	Generates audio

This makes the system modular, scalable, and easy to maintain.

🔹 LLM Engine – Ollama + LLaMA 3.2

Ollama runs large language models locally.

Why Ollama?

Full data privacy

No paid APIs

Faster response

Works offline

Model Used: LLaMA 3.2

Used for:

Medical reasoning

Explanation

Summarization

Translation prompts

🔹 Text-to-Speech

Uses gTTS (Google Text-to-Speech)
Converts explanations into audio files.

Useful for:

Visually impaired users

Elderly patients

Audio-based understanding

Audio files are stored in the audio/ directory.

🔹 Background Processing

OCR, AI inference, translation, and audio generation run using FastAPI BackgroundTasks.

Benefits

Faster API responses

Non-blocking execution

Better scalability

Smooth user experience


📁 Project Structure

```text  ai-medical-report-agent/
│
├── app/
│   ├── main.py                 # FastAPI entry point
│
│   ├── core/                   # Config & security
│   │   ├── config.py
│   │   ├── security.py
│   │   └── deps.py
│
│   ├── db/                     # Database layer
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│
│   ├── models/                 # ORM models
│   │   ├── user.py
│   │   ├── report.py
│   │   └── analysis.py
│
│   ├── schemas/                # Pydantic schemas
│   │   ├── user.py
│   │   ├── auth.py
│   │   └── report.py
│
│   ├── auth/                   # Authentication
│   │   ├── jwt.py
│   │   ├── hashing.py
│   │   └── routes.py
│
│   ├── agents/                 # AI agents
│   │   ├── medical_agent.py
│   │   ├── explain_agent.py
│   │   ├── translate_agent.py
│   │   └── voice_agent.py
│
│   ├── services/               # Business logic
│   │   ├── llm_service.py
│   │   ├── report_processor.py
│   │   ├── translation_service.py
│   │   └── tts_service.py
│
│   ├── ocr/                    # OCR pipeline
│   │   ├── pdf_reader.py
│   │   ├── image_reader.py
│   │   └── clean_text.py
│
│   ├── api/                    # API routes
│   │   ├── report_routes.py
│   │   └── history_routes.py
│
│   └── utils/                  # Helpers
│       ├── file_utils.py
│       └── response_utils.py
│
├── uploads/                    # Uploaded reports
├── audio/                      # Generated audio
├── requirements.txt
├── .env
└── README.md   ```


🧠 High-Level System Flow

```text

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
Database Storage + Audio File   ```


▶️ How to Run the Project


1️⃣ Clone the Repository
git clone (https://github.com/Sumit-123singh/AI-Medical-Report-Analyzer-Agent)
cd ai-medical-report-agent

2️⃣ Create Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Server
uvicorn app.main:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs



👤 Author
Sumit Singh

Backend & AI Engineer

Focused on building scalable backend systems and AI-powered healthcare applications using FastAPI, OCR pipelines, LLMs, and clean architecture principles.

