from pydantic import BaseModel, Field
from typing import Optional


class ProposalRequest(BaseModel):
    niche: str = Field(
        min_length=2,
        max_length=120
    )

    client_problem: str = Field(
        min_length=10,
        max_length=1000
    )

    tone: str = Field(
        min_length=2,
        max_length=50
    )

    platform: str = Field(
        min_length=2,
        max_length=50
    )


class ProposalResponse(BaseModel):
    proposal: str
    cta: str
    subject_line: str
    follow_up: str


class ProposalHistoryResponse(BaseModel):
    id: int
    niche: str
    platform: str
    created_at: str


class ErrorResponse(BaseModel):
    detail: str
