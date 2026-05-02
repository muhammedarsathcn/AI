import httpx

async def fetch_dictionary_meaning(word:str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if(response.status_code != 200):
            return{}
        data = response.json()
        meanings = []
        phonetic = ""

        for entry in data:
            phonetic = entry.get("phonetic","")
            for meaning in entry.get("meanings",[]):
                meanings.append(
                    {
                        "part_of_speech": meaning["partOfSpeech"],
                        "definition": meaning["definitions"][0]["definition"]
                    }
                )
        
        return {
            "phonetic":phonetic,
            "meanings":meanings
        }