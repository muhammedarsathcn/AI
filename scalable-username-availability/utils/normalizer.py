import re

def normalize( username):
    username = username.strip()
    username = username.lower()
    username = re.sub(r"\s+","_",username) # type: ignore
    return username