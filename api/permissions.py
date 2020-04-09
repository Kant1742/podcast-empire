from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # RUD permissions are available only to the author
        return obj.user == request.user
