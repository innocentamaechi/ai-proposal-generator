from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request

from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Proposal


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/")
async def home(
    request: Request,
    db: Session = Depends(get_db)
):

    history = (
        db.query(Proposal)
        .order_by(Proposal.created_at.desc())
        .limit(10)
        .all()
    )

    formatted_history = [
        {
            "niche": item.niche,
            "platform": item.platform,
            "created_at": item.created_at.strftime(
                "%Y-%m-%d %H:%M"
            )
        }
        for item in history
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "history": formatted_history
        }
    )
