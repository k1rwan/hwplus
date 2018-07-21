# Create your views here.
from rest_framework import viewsets
from data import models
from data.models import User
from data import serializers
from data import permissions
from project.settings import API_AUTH_KEY, SECRET_KEY
from data.confirm import Token, ShortToken
from data.confirm import send
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from itsdangerous import SignatureExpired
import re

token = Token(SECRET_KEY.encode())
short_token=ShortToken(SECRET_KEY.encode())
results={
    'SUCCESS':{
        'code':1000,
        'msg':'success'
    },
    'INACTIVE':{
        'code':4020,
        'msg':'用户未激活'
    },
    'EXPIRED':{
        'code':4030,
        'msg':'身份验证过期，请重新登录',
    },
    'PWD_ERR':{
        'code':4040,
        'msg':'用户名或密码错误'
    }
}

data = None
headers = None

def init():
    global data,headers
    data = {
        'result': {
            'code':None,
            'msg':None
        },
        'data': None
    }
    headers = {
        'token': None
    }

class HWFCourseClassViewSet(viewsets.ModelViewSet):
    queryset = models.HWFCourseClass.objects.all()
    serializer_class = serializers.HWFCourseClassSerializer


class HWFAssignmentViewSet(viewsets.ModelViewSet):
    queryset = models.HWFAssignment.objects.all()
    serializer_class = serializers.HWFAssignmentSerializer


class HWFFileViewSet(viewsets.ModelViewSet):
    queryset = models.HWFFile.objects.all()
    serializer_class = serializers.HWFFileSerializer


class HWFSubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.HWFSubmission.objects.all()
    serializer_class = serializers.HWFSubmissionSerializer


class HWFQuestionViewSet(viewsets.ModelViewSet):
    queryset = models.HWFQuestion.objects.all()
    serializer_class = serializers.HWFQuestionSerializer


class HWFAnswerViewSet(viewsets.ModelViewSet):
    queryset = models.HWFAnswer.objects.all()
    serializer_class = serializers.HWFAnswerSerializer


class HWFReviewViewSet(viewsets.ModelViewSet):
    queryset = models.HWFReview.objects.all()
    serializer_class = serializers.HWFReviewSerializer
