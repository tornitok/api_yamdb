from rest_framework.exceptions import PermissionDenied
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


class IsAdminOrModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.role == User.Roles.ADMIN
                or request.user.role == User.Roles.MODERATOR)


class isNotUserRole(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_authenticated
            and request.user.role == User.Roles.USER
            and not request.user.is_superuser):
            raise PermissionDenied(
                f'Недостаточно прав для данного действия'
            )
                    
        return True


class isNotModeratorRole(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_authenticated
            and request.user.role == User.Roles.MODERATOR
            and not request.user.is_superuser):
            raise PermissionDenied(
                f'Недостаточно прав для данного действия'
            )
                    
        return True


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