import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 🔥 Explicitly load .env from project root
BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(f"OPENAI_API_KEY not found. Checked path: {ENV_PATH}")

client = OpenAI(api_key=api_key)



def is_drug_discovery_company(description: str) -> bool:
    prompt = f"""
    Company description:
    {description}

    Question:
    Is this company involved in drug discovery or biomedical research?
    Answer only Yes or No.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    answer = response.choices[0].message.content.lower()
    return "yes" in answer
