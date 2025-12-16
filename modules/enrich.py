from utils.pubmed import has_recent_pubmed_paper
from utils.ai_enrich import is_drug_discovery_company

def enrich_lead(lead):
    # ---- Funding logic (mock) ----
    if "Director" in lead.title:
        lead.funding_stage = "Series B"
    else:
        lead.funding_stage = "Bootstrapped"

    # ---- Real PubMed signal ----
    lead.recent_publication = has_recent_pubmed_paper(
        author_name=lead.name
    )

    # ---- AI enrichment ----
    company_description = (
        f"{lead.company} works on biomedical research and drug safety models."
    )

    lead.drug_discovery_company = is_drug_discovery_company(
        company_description
    )

    return lead
