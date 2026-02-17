from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only owner can edit/delete.
    Others can only read.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods (GET, HEAD, OPTIONS) allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only for owner
        return obj.created_by == request.user
