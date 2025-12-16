from config import WEIGHTS

def score_lead(lead):
    score = 0
    reasons = []

    if "Director" in lead.title:
        score += WEIGHTS["director_role"]
        reasons.append("Decision-maker role")

    if lead.funding_stage in ["Series A", "Series B"]:
        score += WEIGHTS["funded_company"]
        reasons.append("Company has funding")

    if lead.recent_publication:
        score += WEIGHTS["recent_publication"]
        reasons.append("Recent scientific publication")

    if lead.company_hq and "Cambridge" in lead.company_hq:
        score += WEIGHTS["hub_location"]
        reasons.append("Located in biotech hub")

    if lead.drug_discovery_company:
        score += WEIGHTS["drug_discovery_match"]
        reasons.append("Company involved in drug discovery")

    lead.score = min(score, 100)
    lead.score_reasons = reasons

    return lead
