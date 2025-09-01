from rest_framework import permissions


class IsOwnerOrAdminOrCreateOnly(permissions.BasePermission):
        
        
    def has_permission(self, request, view):
        # Allow anyone to create a user (POST)
        if view.action == "create":
            return True
        
        # Allow authenticated users to view list
        if view.action in ["list", "retrieve"]:
            return request.user and request.user.is_authenticated
        
        # For update/delete actions, require authentication
        # (specific permission check happens in has_object_permission)
        if view.action in ["update", "partial_update", "destroy"]:
            return request.user and request.user.is_authenticated
        
        # Default deny for any other actions
        return False

    def has_object_permission(self, request, view, obj):
        # Admins can do anything
        if request.user.is_staff:
            return True
        
        # Users can only update/delete their own account
        if view.action in ["update", "partial_update", "destroy"]:
            return obj == request.user
        
        # Authenticated users can view any user's details
        if view.action == "retrieve":
            return request.user.is_authenticated
        
        return False