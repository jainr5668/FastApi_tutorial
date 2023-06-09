from typing import List, Optional
from pydantic import BaseModel

class GamePostSchema(BaseModel):
    name: str
    description: str
    no_of_players: int
    is_indoor: bool
    is_team_game: bool


class GamePostSchemaUpdated(GamePostSchema):
    id: int

    class Config:
        orm_mode = True

class GamePostResponseSchema(BaseModel):
    id: int
    data: GamePostSchemaUpdated


class GameGetAllSchema(BaseModel):
    length: int
    data: List[GamePostSchemaUpdated]

class GamePatchSchema(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    no_of_players: Optional[int]
    is_indoor: Optional[bool]
    is_team_game: Optional[bool]