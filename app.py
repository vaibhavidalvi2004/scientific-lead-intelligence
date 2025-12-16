import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd

from modules.identify import identify_leads
from modules.enrich import enrich_lead
from modules.score import score_lead

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Scientific Lead Intelligence",
    page_icon="🔬",
    layout="wide"
)

# ---------------- GLOBAL STYLING ----------------
st.markdown("""
<style>

/* 🌊 Soft scientific blue background */
.stApp {
    background: linear-gradient(
        180deg,
        #f4f7ff 0%,
        #eef3ff 50%,
        #f9fbff 100%
    );
}

/* Main titles */
h1 {
    color: #0f2a44;
}
h2, h3 {
    color: #163a5f;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #ffffff;
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}

/* Metric values */
[data-testid="stMetricValue"] {
    font-size: 28px;
}

/* Dataframe styling */
[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.10);
}

/* Download button */
.stDownloadButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 600;
}
.stDownloadButton button:hover {
    background-color: #1e40af;
}

/* Input fields */
input {
    border-radius: 10px !important;
}

/* Divider */
hr {
    border-top: 2px solid #e5e7eb;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HELPER FUNCTIONS ----------------
def confidence(score):
    if score >= 80:
        return "🟢 High"
    elif score >= 50:
        return "🟡 Medium"
    return "🔴 Low"

# ---------------- HEADER CARD ----------------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #1e3a8a, #2563eb);
    padding: 28px;
    border-radius: 18px;
    color: white;
">
    <h1>🔬 Scientific Lead Intelligence Dashboard</h1>
    <p style="font-size:16px; margin-top:8px;">
        Identify, enrich, and prioritize high-value scientific decision-makers using AI and PubMed signals.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- BUILD PIPELINE ----------------
leads = identify_leads()
leads = [score_lead(enrich_lead(l)) for l in leads]

df = pd.DataFrame([l.dict() for l in leads])
df = df.sort_values("score", ascending=False)
df["confidence"] = df["score"].apply(confidence)

# ---------------- METRICS ----------------
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Total Leads", len(df))

with m2:
    st.metric("High Confidence", (df["confidence"] == "🟢 High").sum())

with m3:
    st.metric("Average Score", round(df["score"].mean(), 1))

st.divider()

# ---------------- SEARCH & FILTER ----------------
st.subheader("🔎 Search & Filter")

search = st.text_input(
    "Search by name, title, company, or location",
    placeholder="e.g. Director, Cambridge, Toxicology"
)

if search:
    df = df[df.apply(
        lambda row: search.lower() in row.astype(str).str.lower().to_string(),
        axis=1
    )]

# ---------------- TABLE ----------------
df = df[
    [
        "score",
        "confidence",
        "name",
        "title",
        "company",
        "person_location",
        "company_hq",
        "email",
        "linkedin_url"
    ]
]

st.subheader("🏆 Prioritized Leads")

st.dataframe(
    df,
    use_container_width=True,
    height=360
)

# ---------------- EXPLAINABILITY ----------------
st.divider()
st.subheader("🔍 Why did this lead score this way?")

if not df.empty:
    selected = st.selectbox(
        "Select a lead",
        df["name"].tolist()
    )

    reasons = next(
        l["score_reasons"] for l in [lead.dict() for lead in leads]
        if l["name"] == selected
    )

    for r in reasons:
        st.markdown(
            f"""
            <div style="
                background-color:#ecfdf5;
                padding:12px 16px;
                border-left:6px solid #10b981;
                border-radius:10px;
                margin-bottom:10px;
            ">
            ✅ <strong>{r}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- DOWNLOAD ----------------
st.divider()
st.download_button(
    "⬇️ Download Ranked Leads (CSV)",
    df.to_csv(index=False),
    "ranked_leads.csv",
    use_container_width=True
)
