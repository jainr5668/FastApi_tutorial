from typing import List
from pydantic import BaseModel

class EventPostSchema(BaseModel):
    name:str
    description: str

class EventPostSchemaUpdated(EventPostSchema):
    id:int
    class Config:
        orm_mode = True

class EventPostResponseSchema(BaseModel):
    id:int
    data:EventPostSchemaUpdated

class EventGetAllSchema(BaseModel):
    length:int
    data:List[EventPostSchemaUpdated]
