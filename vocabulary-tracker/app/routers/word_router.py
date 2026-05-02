from fastapi import APIRouter, Depends, status, Query, HTTPException
from app.dependencies.auth_dependency import get_current_user
from app.schemas.word_schema import WordCreate, WordUpdate, WordResponse
from typing import Optional, List 
from app.services.word_service import create_word, get_word_by_id, get_all_words,update_word,delete_word

router = APIRouter(
    prefix="/words",
    tags=["Words"]
)



@router.post("/", status_code=status.HTTP_201_CREATED)
def add_word(payload:WordCreate, user = Depends(get_current_user)):
    return create_word(payload)

@router.get("/", response_model = List[WordResponse])
def list_words(mastered:Optional[bool] = Query(None), user = Depends(get_current_user)):
    return get_all_words(mastered)

@router.get("/{word_id}")
async def get_word(word_id:int, user=Depends(get_current_user)):
    result = await get_word_by_id(word_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Word not found"
        )
    return result

@router.patch("/{word_id}")
def edit_word(word_id:int, payload:WordUpdate, user = Depends(get_current_user)):
    updated = update_word(word_id, payload)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Word not found"
        )
    return updated

@router.delete("/{word_id}")
def remove_word(word_id:int ,user =Depends(get_current_user)):
    deleted = delete_word(word_id)
    if not deleted:
          raise HTTPException(
            status_code=404,
            detail="Word not found"
        )
    return deleted