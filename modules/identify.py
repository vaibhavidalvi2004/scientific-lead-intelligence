from app_models.lead import Lead

# NOTE:
# Currently using mock leads.
# In production, this will be replaced with:
# - CRM ingestion
# - LinkedIn scraping
# - Conference attendee lists
# - PubMed author search


def identify_leads():
    return [
        Lead(
            name="Dr. Alice Brown",
            title="Director of Toxicology",
            company="BioThera Inc",
            person_location="Colorado",
            company_hq="Cambridge, MA",
            email="alice@biothera.com",
            linkedin_url="https://linkedin.com/in/alice-brown"
        ),
        Lead(
            name="Dr. Mark Lee",
            title="Senior Scientist",
            company="SmallBio",
            person_location="Texas",
            company_hq="Austin, TX",
            email="mark@smallbio.com",
            linkedin_url="https://linkedin.com/in/mark-lee"
        ),
        Lead(
            name="Dr. Sarah Kim",
            title="VP Research",
            company="NeuroGenix",
            person_location="California",
            company_hq="San Diego, CA",
            email="sarah@neurogenix.com",
            linkedin_url="https://linkedin.com/in/sarah-kim"
        ),
        Lead(
            name="Dr. Rahul Mehta",
            title="Director of Drug Discovery",
            company="PharmaNext",
            person_location="New Jersey",
            company_hq="Boston, MA",
            email="rahul@pharmanext.com",
            linkedin_url="https://linkedin.com/in/rahul-mehta"
        )
    ]

