from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from .. import base


class EventPostModel(base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    class Config:
        orm_mode = True

