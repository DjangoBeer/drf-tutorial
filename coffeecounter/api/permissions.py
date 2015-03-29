from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow superusers to edit objects.
    """

    def has_permission(self, request, view):
         # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # You need to be superuser to do POST, PUT and PATCH requests.
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # You need to be superuser to do POST, PUT and PATCH requests.
        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user
