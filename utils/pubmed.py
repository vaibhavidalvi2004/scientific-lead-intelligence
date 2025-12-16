from Bio import Entrez
from datetime import datetime
import re

Entrez.email = "test@example.com"

def has_recent_pubmed_paper(author_name: str, years: int = 2) -> bool:
    """
    Safely checks if an author has a recent PubMed paper.
    Handles messy PubMed date formats.
    """

    query = f'{author_name}[Author]'
    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=1,
        sort="pub date"
    )
    results = Entrez.read(handle)
    handle.close()

    if not results["IdList"]:
        return False

    handle = Entrez.efetch(
        db="pubmed",
        id=results["IdList"][0],
        rettype="medline",
        retmode="text"
    )
    record = handle.read()
    handle.close()

    current_year = datetime.now().year

    for line in record.split("\n"):
        if line.startswith("DP"):
            # Extract first 4-digit year safely
            match = re.search(r"\b(19|20)\d{2}\b", line)
            if not match:
                return False

            year = int(match.group())
            return (current_year - year) <= years

    return False
