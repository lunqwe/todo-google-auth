import requests
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


def error_detail(e):
    errors = e.detail
    
    error_messages = []
    for field, messages in errors.items():
        error_messages.append(f'{field}: {messages[0].__str__()}')
    
    return error_messages

def check_expired_tokens(user: User) -> bool:
    """
    Checks if user`s token is expired (for deleting expired tokens)
    """
    tokens = OutstandingToken.objects.filter(user_id=user.id)
    if tokens:
        [token.delete() for token in tokens]
        
    return True
    
def get_user_jwt(user: User):
    """ Creating JWT tokens for User 
    
    Function is using a library djangorestframework-simple-jwt
    (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)

    Args:
        user (User): object of User model (.models.User)

    Returns:
        Function returns two JWT tokens (access & refresh)
    """
    # checking if there are expired tokens (to delete them)
    check_expired_tokens(user)
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
def get_google_data(id_token: str) -> dict:
    """
    Function requests user`s data from google

    Args:
        id_token (str): user id_token

    Raises:
        ConnectionRefusedError: if token is wrong

    Returns:
        dict: user data
    """
    
    response = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}')
    if response.status_code != 200:
        raise ConnectionRefusedError('Invalid token')
    return response.json()
