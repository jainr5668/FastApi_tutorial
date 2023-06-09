from sqlalchemy import Boolean, Integer, Column, String, DateTime
from .. import base


class GamePostModel(base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    no_of_players = Column(Integer, nullable=False)
    is_indoor = Column(Boolean, nullable=False)
    is_team_game = Column(Boolean, nullable=False, default=True)

    class Config:
        orm_mode = True
