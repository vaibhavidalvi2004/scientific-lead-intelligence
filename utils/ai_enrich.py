def is_drug_discovery_company(company_description: str) -> bool:
    """
    AI enrichment placeholder.

    Disabled in Streamlit Cloud to avoid external API calls.
    Can be re-enabled in local / production backend.
    """
    description = company_description.lower()
    return "drug" in description or "biomedical" in description or "pharma" in description
