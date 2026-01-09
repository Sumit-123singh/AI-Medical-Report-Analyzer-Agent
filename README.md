


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

