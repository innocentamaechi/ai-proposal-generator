from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request

from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Proposal

from app.schemas.proposal_schema import ProposalRequest
from app.schemas.proposal_schema import ProposalResponse

from app.services.proposal_service import ProposalService

from app.config.logging_config import get_logger


logger = get_logger()

router = APIRouter(
    prefix="/api",
    tags=["API"]
)


@router.post(
    "/generate",
    response_model=ProposalResponse
)
async def generate_proposal(
    payload: ProposalRequest,
    request: Request,
    db: Session = Depends(get_db)
):

    try:

        ai_response = ProposalService.generate_proposal(
            niche=payload.niche,
            client_problem=payload.client_problem,
            tone=payload.tone,
            platform=payload.platform
        )

        proposal_record = Proposal(
            niche=payload.niche,
            client_problem=payload.client_problem,
            tone=payload.tone,
            platform=payload.platform,
            proposal=ai_response["proposal"],
            cta=ai_response["cta"],
            subject_line=ai_response["subject_line"],
            follow_up=ai_response["follow_up"],
            ip_address=request.client.host
        )

        db.add(proposal_record)
        db.commit()

        logger.info(
            f"Proposal generated successfully "
            f"for niche={payload.niche}"
        )

        return ProposalResponse(
            proposal=ai_response["proposal"],
            cta=ai_response["cta"],
            subject_line=ai_response["subject_line"],
            follow_up=ai_response["follow_up"]
        )

    except ValueError as error:

        logger.warning(str(error))

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except RuntimeError as error:

        logger.error(str(error))

        raise HTTPException(
            status_code=503,
            detail="AI service temporarily unavailable"
        )

    except Exception as error:

        logger.error(str(error))

        raise HTTPException(
            status_code=500,
            detail="Failed to generate proposal"
        )


@router.get("/history")
async def proposal_history(
    db: Session = Depends(get_db)
):

    records = (
        db.query(Proposal)
        .order_by(Proposal.created_at.desc())
        .limit(10)
        .all()
    )

    return [
        {
            "id": item.id,
            "niche": item.niche,
            "platform": item.platform,
            "created_at": item.created_at.strftime(
                "%Y-%m-%d %H:%M"
            )
        }
        for item in records
    ]
