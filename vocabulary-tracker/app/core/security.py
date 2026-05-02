from jose import jwt

SECRET_KEY = "secretKey"
ALGORITHM = "HS256"

def create_access_token(payload:dict):
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )