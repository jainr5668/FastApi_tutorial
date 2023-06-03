from sqlalchemy import Integer, Column, String, DateTime
from .. import base


class EventPostModel(base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    max_player = Column(Integer, nullable=False)
    min_player = Column(Integer, nullable=False)

    class Config:
        orm_mode = True
