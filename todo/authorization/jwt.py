from datetime import datetime, timedelta

from django.conf import settings

import jwt

from todo.utils.custom_exception import InvalidTokenException


def generate_jwt_token(user):
    payload = {
        "user_id": user["id"],
        "email": user["email"],
        "exp": datetime.utcnow() + timedelta(minutes=60),
        "iat": datetime.utcnow(),
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")
    return token


def decode_jwt_token(token):
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise InvalidTokenException("Token has expired")
    except jwt.InvalidTokenError:
        raise InvalidTokenException("Invalid token")


def refresh_jwt_token(token):
    payload = decode_jwt_token(token)
    if isinstance(payload, str):
        return payload
    user_id = payload["user_id"]
    email = payload["email"]
    new_payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=15),
        "iat": datetime.utcnow(),
    }
    new_token = jwt.encode(
        new_payload, settings.JWT_SECRET_KEY, algorithm="HS256"
    )
    return new_token.decode("utf-8")
