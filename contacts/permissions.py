from rest_framework.permissions import BasePermission
from contacts.decorators import validate_token


class IsUserLogin(BasePermission):
    @validate_token
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
