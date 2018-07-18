from rest_framework import permissions
from data.confirm import send

class AbleToCreate(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method=='POST' and request.user is obj:
            send(request.user)
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False
