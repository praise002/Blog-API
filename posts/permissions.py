from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        #a tuple containing GET, OPTIONS & HEAD then it is a read-only request, permission is granted
        if request.method in permissions.SAFE_METHODS:  
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user