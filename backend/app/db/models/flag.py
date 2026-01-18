from sqlalchemy import Column, Integer, String, ForeignKey

from backend.app.db.base import Base


class Flag(Base):
    __tablename__ = "flags"

    id = Column(Integer, primary_key=True, index=True)

    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    hash = Column(String(255), nullable=False)
