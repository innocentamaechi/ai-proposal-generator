from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from app.database.db import Base


class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True, index=True)

    niche = Column(String(120), nullable=False)

    client_problem = Column(Text, nullable=False)

    tone = Column(String(50), nullable=False)

    platform = Column(String(50), nullable=False)

    proposal = Column(Text, nullable=False)

    cta = Column(Text, nullable=False)

    subject_line = Column(String(255), nullable=False)

    follow_up = Column(Text, nullable=False)

    ip_address = Column(String(120), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
