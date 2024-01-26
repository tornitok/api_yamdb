from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import User


class IsAuthorOrAdminOrModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user == obj.author
                or request.user.role == User.Roles.ADMIN
                or request.user.role == User.Roles.MODERATOR)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and request.user.role == User.Roles.ADMIN
            or user.is_superuser
        )


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated and request.user.is_superuser)