from sqlalchemy import Column, Integer, ForeignKey, String

from backend.app.db.base import Base


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    completed_tasks = Column(String, nullable=False, default="")
