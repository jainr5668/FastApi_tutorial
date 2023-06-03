from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship, mapped_column

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
