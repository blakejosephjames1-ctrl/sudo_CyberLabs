from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.db.base import Base


class LabInstance(Base):
    __tablename__ = "lab_instances"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    vm_ids = Column(String, nullable=False)
    network_id = Column(String, nullable=False)

    status = Column(String(20), nullable=False, default="running")
    expires_at = Column(DateTime, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User")
    room = relationship("Room")