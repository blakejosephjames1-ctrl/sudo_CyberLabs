from sqlalchemy import Column, Integer, String
from backend.app.db.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    """User model for authentication and user management."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"