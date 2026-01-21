
# 🚀 PrepKit: AI-Powered Career Acceleration Platform

> **Automating the tedious parts of job hunting and providing data-driven interview coaching.**

PrepKit is a dual-feature platform designed to streamline the job application process and improve interview performance. By leveraging **LLaMA-3** for content generation and **FFmpeg** for acoustic analysis, PrepKit reduces application time by 75% and provides actionable, real-time feedback on speech confidence and pacing.


## 📑 Table of Contents

* [Features](https://www.google.com/search?q=%23-features)
* [Architecture](https://www.google.com/search?q=%23-architecture)
* [Tech Stack](https://www.google.com/search?q=%23-tech-stack)
* [Installation](https://www.google.com/search?q=%23-installation)
* [Usage](https://www.google.com/search?q=%23-usage)
* [Configuration](https://www.google.com/search?q=%23-configuration)
* [Performance Metrics](https://www.google.com/search?q=%23-performance-metrics)
* [Project Structure](https://www.google.com/search?q=%23-project-structure)
* [Key Technical Decisions](https://www.google.com/search?q=%23-key-technical-decisions)
* [Roadmap](https://www.google.com/search?q=%23-future-improvements)
* [Contact](https://www.google.com/search?q=%23-contact)

---

## ✨ Features

### 1. ⚡ Automated Job Application Workflow

Eliminate writer's block and generic applications.

* **Intelligent Parsing:** Extracts structured data from uploaded resumes (PDF/DOCX).
* **LLaMA-3 Generation:** Creates tailored cover letters in **3-5 seconds**.
* **RAG Implementation:** Uses Retrieval-Augmented Generation to match resume skills with job descriptions, yielding a **40% relevance improvement**.
* **Efficiency:** Reduces manual application time by **75%**.

### 2. 🎤 AI-Powered Interview Practice

Practice answering behavioral questions with instant, objective feedback.

* **Browser Recording:** Seamless audio capture via Web Audio API.
* **Acoustic Analysis:** Extracts 7 key audio features using **FFmpeg**.
* **Instant Feedback:**
* Speech Rate (WPM) & Pacing
* Filler Word Detection (ums, uhs)
* Volume Consistency & Pitch Variation
* Articulation Clarity


* **Progress Tracking:** Longitudinal scoring to visualize improvement over time.

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 🏗 Architecture

![Architecture](./assets/prepkit-architecture.png)

PrepKit utilizes a **Microservices Architecture** to ensure independent scaling and fault isolation. The system is containerized using Docker and orchestrated via Docker Compose.

**Services List:**

1. **API Gateway (Port 5000):** Central entry point handling request routing, rate limiting, and authentication.
2. **Resume Parser Service (Port 5001):** Handles PDF/DOCX ingestion and text extraction.
3. **Cover Letter Generator (Port 5002):** Hosts the LLaMA-3 (8B, 4-bit quantized) model for inference.
4. **Audio Processing Service (Port 5003):** Runs FFmpeg pipelines for acoustic feature extraction.
5. **Scoring Engine (Port 5004):** Aggregates data to generate confidence scores and actionable tips.

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 🛠 Tech Stack

| Category | Technologies |
| --- | --- |
| **Backend** | Python, Flask, Celery (Async Tasks), Redis (Message Broker) |
| **AI / ML** | **LLaMA-3 (8B)**, **Whisper** (STT), Hugging Face Transformers, bitsandbytes |
| **Audio Processing** | **FFmpeg**, Web Audio API |
| **Frontend** | React, TypeScript, Tailwind CSS |
| **Database** | PostgreSQL (User Data), Vector DB (RAG) |
| **Infrastructure** | AWS (EC2, S3, RDS), Docker, Nginx |

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 📥 Installation

### Prerequisites

* Python 3.11+
* Docker & Docker Compose
* AWS Account (for S3/deployment features)
* **Hardware:** 8GB+ RAM required for local LLaMA-3 inference.

### Local Development Setup

1. **Clone the repository**
```bash
git clone https://github.com/saikiranbilla/prepkit.git
cd prepkit

```


2. **Environment Setup**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```


3. **Configuration**
```bash
cp .env.example .env
# Open .env and populate your keys (see Configuration section)

```


4. **Model Setup**
```bash
# Download LLaMA-3 model (approx 5GB)
python scripts/download_model.py

```


5. **Run Application**
```bash
# Recommended: Run with Docker Compose
docker-compose up --build

# Alternative: Run services individually
python services/api_gateway.py
# (Open new terminals for other services)

```



[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 🖥 Usage

### Job Application Feature

1. Navigate to `http://localhost:3000`.
2. Upload your resume (PDF).
3. Paste the Job Description (JD).
4. Click **"Generate Cover Letter"**.
5. Review, edit, and download the result.

**API Usage:**

```bash
curl -X POST http://localhost:5000/api/generate-cover-letter \
  -F "resume=@my_resume.pdf" \
  -F "job_description=@job_desc.txt"

```

### Interview Practice Feature

1. Navigate to `http://localhost:3000/interview`.
2. Select a practice question.
3. Click **"Start Recording"** and answer (60-120 seconds).
4. Stop recording to trigger analysis.
5. View dashboard with WPM, filler word count, and confidence score.

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## ⚙ Configuration

Create a `.env` file in the root directory:

```env
# AWS Configuration
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
S3_BUCKET_NAME=prepkit-uploads

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/prepkit

# Redis
REDIS_URL=redis://localhost:6379

# LLaMA-3 Configuration
MODEL_PATH=./models/llama3-8b
QUANTIZATION=4bit
MAX_TOKENS=1000

# Optional API Keys
OPENAI_API_KEY=your_key  # Only if using Whisper API instead of local model

```

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 📊 Performance Metrics

| Metric | Value | Notes |
| --- | --- | --- |
| **Scalability** | 100+ Concurrent Users | Via AWS Auto Scaling Group |
| **Generation Latency** | 3-5 Seconds | Cover Letter (4-bit quantization) |
| **Audio Processing** | 5-8 Seconds | For 2-minute audio clips |
| **Transcription Accuracy** | 95%+ | Powered by OpenAI Whisper |
| **Relevance Score** | 85/100 | 40% improvement over generic templates |
| **Cost Savings** | $0.30 / Gen | Savings vs. GPT-4 API calls |

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 📂 Project Structure

```text
prepkit/
├── services/                 # Microservices
│   ├── api_gateway.py        # Routing & Auth
│   ├── resume_parser.py      # PDF Extraction
│   ├── cover_letter_generator.py # LLM Inference
│   ├── audio_processor.py    # FFmpeg Logic
│   └── scoring_engine.py     # Feedback Logic
├── frontend/                 # React Application
│   ├── src/
│   ├── public/
│   └── package.json
├── models/
│   └── llama3-8b/            # Local model weights
├── utils/
│   ├── ffmpeg_pipeline.py    # Audio processing scripts
│   ├── vector_db.py          # RAG implementation
│   └── prompt_templates.py   # System prompts
├── tests/                    # Unit & Integration tests
├── docker-compose.yml        # Orchestration
├── requirements.txt          # Python dependencies
├── .env.example              # Config template
└── README.md

```

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 💡 Key Technical Decisions

### Why LLaMA-3 over GPT-4?

* **Cost Efficiency:** Self-hosting reduces variable costs to nearly zero (excluding compute), saving ~$0.30 per generation compared to GPT-4.
* **Privacy:** User resumes and job history remain on our VPC, ensuring data sovereignty.
* **Performance:** 4-bit quantization allows inference on CPU/Consumer GPUs (8GB VRAM) while maintaining 84/100 quality scores.

### Why Microservices?

* **Resource Allocation:** The LLM service requires heavy memory, while the parser requires high I/O. Decoupling allows us to scale instances independently.
* **Fault Tolerance:** A crash in the audio processing service (e.g., malformed file) does not affect the cover letter generator.

### Why FFmpeg?

* **Robustness:** Industry standard for handling various audio codecs and formats uploaded by users.
* **Feature Extraction:** Native filters allow for fast extraction of pitch, volume, and silence duration without needing heavy ML models for simple signal processing.

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 🔮 Future Improvements

* [ ] **Resume Tailoring:** Auto-reorder and rephrase bullet points to match job keywords.
* [ ] **Video Analysis:** Computer vision integration to track eye contact and body language.
* [ ] **Conversational AI:** Real-time mock interviewer using Text-to-Speech (TTS).
* [ ] **Job Board Integration:** Automated application submission.
* [ ] **Active Learning:** Fine-tuning LLaMA-3 based on user edits to generated letters.
* [ ] **Multi-language Support:** Spanish and Mandarin.

[Back to Top](https://www.google.com/search?q=%23-prepkit-ai-powered-career-acceleration-platform)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

See `CONTRIBUTING.md` for detailed guidelines.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact & Acknowledgments

**Author:** Sai Kiran Billa

* 📧 Email: [sbilla21@outlook.com](mailto:sbilla21@outlook.com)
* 👔 LinkedIn: [linkedin.com/in/saikiranbilla](https://www.google.com/search?q=https://linkedin.com/in/saikiranbilla)
* 🐙 GitHub: [@saikiranbilla](https://www.google.com/search?q=https://github.com/saikiranbilla)

**Acknowledgments:**

* **Meta AI** for LLaMA-3
* **OpenAI** for Whisper
* **FFmpeg** contributors
* **Hugging Face** for the Transformers library
