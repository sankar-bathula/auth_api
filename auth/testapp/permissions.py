from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
class Permission(BasePermission):
    def has_permission(self,request,view):
        username=request.user.username
        if username.lower()=='himavardhan':
            return True
        elif username!='' and len(username)%2==0 and request.method in SAFE_METHODS:
            return True
        else:
            return False
