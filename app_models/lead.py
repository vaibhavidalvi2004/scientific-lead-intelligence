from pydantic import BaseModel
from typing import Optional, List

class Lead(BaseModel):
    name: str
    title: str
    company: str

    person_location: Optional[str] = None
    company_hq: Optional[str] = None
    email: Optional[str] = None
    linkedin_url: Optional[str] = None

    funding_stage: Optional[str] = None
    recent_publication: bool = False
    drug_discovery_company: bool = False

    score: int = 0
    score_reasons: List[str] = []
