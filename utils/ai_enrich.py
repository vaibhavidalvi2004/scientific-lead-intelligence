def is_drug_discovery_company(company_description: str) -> bool:
    """
    Lightweight heuristic used in Streamlit Cloud.
    Avoids external API calls.
    """
    text = company_description.lower()
    return "drug" in text or "biomedical" in text or "pharma" in text
