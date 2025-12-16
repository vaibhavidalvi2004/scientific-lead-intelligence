🔬 Scientific Lead Intelligence Dashboard

An AI-powered dashboard to identify, enrich, score, and prioritize scientific decision-makers for outreach and business development in biotech and life sciences.

This project demonstrates how rule-based intelligence, external scientific signals, and AI enrichment can be combined into an explainable lead scoring system with a production-ready Streamlit UI.

🚀 Live Demo

👉 Streamlit App
https://scientific-lead-intelligence-dwhefb3ka7yptpj7jcmyot.streamlit.app/


🧠 Problem Statement

Business development and research teams often struggle to identify high-value scientific leads among thousands of researchers and professionals.

This project solves that by:

Collecting scientific profiles

Enriching them with publication activity and AI inference

Scoring leads using transparent, explainable logic

Presenting results in an interactive dashboard

🏗️ System Architecture
Lead Identification
        ↓
Lead Enrichment (PubMed + AI)
        ↓
Explainable Scoring Engine
        ↓
Interactive Streamlit Dashboard

✅ Features Implemented
1️⃣ Lead Identification

Mock scientific leads representing biotech researchers and decision-makers

Easily replaceable with real data sources:

CRM systems

Conference attendee lists

LinkedIn scraping

PubMed author search

📁 modules/identify.py

2️⃣ Lead Enrichment

Each lead is enriched using multiple signals:

🔹 Publication Signal (PubMed)

Checks whether a scientist has recent publications

Helps identify active researchers

📁 utils/pubmed.py

🔹 AI-Based Company Enrichment

Uses an LLM to infer whether a company is involved in:

Drug discovery

Biomedical research

Adds contextual intelligence beyond static data

📁 utils/ai_enrich.py
📁 modules/enrich.py

3️⃣ Explainable Lead Scoring Engine

Leads are scored using transparent rules, including:

Decision-making role (Director, VP, etc.)

Recent scientific publications

Funding stage

Location in major biotech hubs

Involvement in drug discovery

Each lead includes:

Score (0–100)

Confidence level (High / Medium / Low)

Human-readable reasons explaining the score

📁 modules/score.py

4️⃣ Interactive Streamlit Dashboard

A production-style UI featuring:

KPI metrics (total leads, average score, confidence distribution)

Search and filtering across all attributes

Ranked lead table

Score explainability (why a lead scored this way)

CSV export

Clean, science-themed design

📁 app.py

⚙️ How to Use This Project
▶️ Run Locally (Full Functionality)

Clone the repository

git clone https://github.com/vaibhavidalvi2004/scientific-lead-intelligence.git
cd scientific-lead-intelligence


Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Set environment variables

OPENAI_API_KEY=your_openai_api_key


Run the app

streamlit run app.py


✅ PubMed + AI enrichment fully enabled locally

☁️ Streamlit Cloud Deployment

The public demo is optimized for:

Fast startup

Stable deployment

No external blocking calls

⚠️ Notes on Enrichment & Deployment
🧬 PubMed Enrichment Note

PubMed-based publication enrichment is implemented as a modular component.

Due to Biopython limitations on Streamlit Cloud, this signal is:

❌ Disabled in the public deployment

✅ Enabled in local development

This demonstrates production-grade fallback handling for external dependencies.

🤖 AI Enrichment Note

Live LLM-based enrichment is disabled in the public demo to:

Avoid latency

Prevent API key exposure

Ensure reliability

All AI enrichment logic is fully implemented and can be re-enabled in local or production environments.

🧪 Tech Stack

Python

Streamlit

Pandas

OpenAI API

PubMed / Biopython

GitHub

📂 Project Structure
lead_intel_app/
│
├── app.py
├── config.py
│
├── modules/
│   ├── identify.py
│   ├── enrich.py
│   └── score.py
│
├── utils/
│   ├── pubmed.py
│   └── ai_enrich.py
│
└── app_models/
    └── lead.py

🧠 Design Philosophy

Explainability first – every score is traceable

Modular architecture – easy to extend or replace components

Production mindset – UI, metrics, export, deployment ready

Ethical & safe – no sensitive personal data used

🔮 Future Improvements

Real-time data ingestion

Multi-source enrichment (LinkedIn, patents, grants)

Learning-based scoring (ML models)

User authentication & role-based views

Outreach recommendations

👤 Author

Vaibhavi
AI / ML • Agentic AI • Scientific Intelligence Systems
