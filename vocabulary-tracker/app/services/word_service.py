from app.storage.memory_store import word_store
from app.storage.memory_store import current_id
from app.utils.dictionary_client import fetch_dictionary_meaning


def create_word(payload):
    from app.storage import memory_store
    entry = {
        "id":memory_store.current_id,
        "word":payload.word,
        "note":payload.note,
        "mastered":False
    }
    word_store.append(entry)
    memory_store.current_id += 1
    return entry


def get_all_words(mastered):
    if mastered is None:
        return word_store
    return(
        word
        for word in word_store
        if word["mastered"] == mastered
    )

async def get_word_by_id(word_id):
    for entry in word_store:
        if entry["id"] == word_id:
            meaning = await fetch_dictionary_meaning(entry["word"])
            return{
                "entry":entry,
                "meaning":meaning
            }
    return None

def update_word(word_id, payload):
    for entry in word_store:
        if entry["id"] == word_id:
            if payload.note is not None:
                entry["note"] = payload.note
            if payload.mastered is not None:
                entry["mastered"] = payload.mastered
            return entry
    return None

def delete_word(word_id):
    for index, entry in enumerate(word_store):
        if entry["id"] == word_id:
            word_store.pop(index)
            return True
    return False