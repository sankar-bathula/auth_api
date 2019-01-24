from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsReadOnlyPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class SunnyPermissions(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        if username.lower() == 'sunny':
            return True
        elif username !='' and len(username) % 2 == 0 and request.method in SAFE_METHODS:
            print(username)
            return True
        else:
            return False
