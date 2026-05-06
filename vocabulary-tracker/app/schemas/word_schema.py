from pydantic import BaseModel
from typing import Optional


class WordCreate(BaseModel):
    word:str
    note:Optional[str] = None

class WordUpdate(BaseModel):
    note:Optional[str]= None
    mastered: Optional[bool] = None

class WordResponse(BaseModel):
    id:int
    word:str
    note:Optional[str]
    mastered:bool