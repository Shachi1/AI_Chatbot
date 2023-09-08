import jwt
from app.utils.env import SECRET_KEY


def generate_token(payload):
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print(token)
    return token
