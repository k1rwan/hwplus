import re

from itsdangerous import SignatureExpired
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from data.models import User
from data.user_views import token


# basic class
class SelfEditUserAppendUserRead(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        vtoken = request.META['HTTP_TOKEN']
        if token.confirm_validate_token(vtoken):
            return True
        return False

# basic class


class SelfEditTeacherAppendUserRead(SelfEditUserAppendUserRead):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        vtoken = request.META['HTTP_TOKEN']
        if User.objects.get(username=token.confirm_validate_token(vtoken)).usertype == 'teacher':
            return True
        return False

# derived


class SelfEditTeacherAppendUserReadForHWFCourseClass(SelfEditTeacherAppendUserRead):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        vtoken = request.META['HTTP_TOKEN']
        if token.confirm_validate_token(vtoken) == User.objects.get(pk=obj.creator_id).username:
            return True
        return False


class SelfEditUserReadForHWFCourseClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method != 'PUT':
            return False
        else:
            vtoken = request.META['HTTP_TOKEN']
            if token.confirm_validate_token(vtoken) == User.objects.get(username=obj.username).username:
                return True
            return False
