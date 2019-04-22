from rest_framework.authtoken.models import Token

from django.core.exceptions import PermissionDenied


def validate_token(function):
    def wrap(request, *args, **kwargs):
        if 'token' in request.COOKIES:
            token = Token.objects.get(key=request.COOKIES['token'])
            if token:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied
    return wrap


