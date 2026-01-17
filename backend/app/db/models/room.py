from sqlalchemy import Column, Integer, String, Text

from backend.app.db.base import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    difficulty = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
