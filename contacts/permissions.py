from tokenize import Token

from rest_framework.permissions import BasePermission


def validate_token(request):
    try:
        if 'token' in request.COOKIES:
            token = Token.objects.get(key=request.COOKIES['token'])
            return token
        else:
            return None
    except Token.DoesNotExist:
        return None


class IsUserLogin(BasePermission):
    def has_object_permission(self, request, view, obj):

        if validate_token(request) is not None:
            return True

        return obj.owner == request.user
