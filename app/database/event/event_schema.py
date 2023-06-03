from fastapi_utils.enums import CamelStrEnum
from enum import auto
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class EventPostSchema(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    max_player: int
    min_player: int


class EventPostSchemaUpdated(EventPostSchema):
    id: int

    class Config:
        orm_mode = True


class EventPostResponseSchema(BaseModel):
    id: int
    data: EventPostSchemaUpdated


class EventGetAllSchema(BaseModel):
    length: int
    data: List[EventPostSchemaUpdated]


class MyEnum(CamelStrEnum):
    choice_one = auto()
    choice_two = auto()


class EventPatchSchema(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    max_player: Optional[int]
    min_player: Optional[int]
