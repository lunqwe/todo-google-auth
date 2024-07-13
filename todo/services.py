from datetime import timedelta, datetime
import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth.models import User
from .serializers import GoogleAuthSerializer


def create_token(user_id: int) -> dict:
    """ A function that creates JWT token 

    Args:
        user_id (int): id of user that requires tokens

    Returns:
        dict: access_token - using create_access_token function that encoding user`s
        data into JWT token
    """
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id}, expires_delta=access_token_expires
        ),
        'token_type': 'Token'
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """A function that creates access JWT token

    Args:
        data (dict): user data that would be encoded into JWT token
        expires_delta (timedelta, optional): datetime when token expires

    Returns:
        _type_: _description_
    """
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire, 'sub': 'access'})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

