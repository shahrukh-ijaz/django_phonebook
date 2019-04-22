from rest_framework.permissions import BasePermission
from contacts.decorators import validate_token


class IsUserLogin(BasePermission):
    @validate_token
    def has_object_permission(self, request, view, obj):

        if validate_token(request) is not None:
            return True

        return obj.owner == request.user
