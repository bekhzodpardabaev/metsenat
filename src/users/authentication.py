from .models import Token
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None
        user_token = Token.objects.filter(key=token.split()[1])
        if not user_token:
            raise exceptions.AuthenticationFailed('Invalid token')
        user = user_token.first().user
        return (user, None)
