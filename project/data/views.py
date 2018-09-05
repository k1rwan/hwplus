# -*- coding: utf-8 -*-
import re
import qrcode
from itsdangerous import SignatureExpired
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from data import models, permissions, serializers
from data.confirm import ShortToken, Token, send
from data.models import User
from project.settings import API_AUTH_KEY, SECRET_KEY, FRONTEND_DOMAIN, BACKEND_DOMIAN

# 一些非REST的接口

token = Token(SECRET_KEY.encode())
short_token = ShortToken(SECRET_KEY.encode())
results = {
    'SUCCESS': {
        'code': 1000,
        'msg': 'success'
    },
    'INACTIVE': {
        'code': 4020,
        'msg': '用户未激活'
    },
    'EXPIRED': {
        'code': 4030,
        'msg': '身份验证过期，请重新登录',
    },
    'PWD_ERR': {
        'code': 4040,
        'msg': '用户名或密码错误'
    }
}

data = None
headers = None


def init():
    global data, headers
    data = {
        'result': {
            'code': None,
            'msg': None
        },
        'data': None
    }
    headers = {
        'token': None
    }

@api_view(['POST'])
def get_qrcode(request):
    qr = qrcode.make("http://"+BACKEND_DOMIAN+"/data/courses/"+str(request.data['course_id']))
    name = short_token.generate_validate_token(str(request.data['course_id']))
    qr.save("./data/backend_media/invitation_qr/"+name+".jpg")
    return Response(data={"qrcode":"http://"+BACKEND_DOMIAN+"/media/invitation_qr/"+name+".jpg","vtk":name})

@api_view(['POST'])
def bind_wechat(request):
    qr = qrcode.make("http://"+BACKEND_DOMIAN+"data/users/"+str(request.data['user_id']))
    name = short_token.generate_validate_token(str(request.data['user_id']))
    qr.save("./data/backend_media/bind_qr/"+name+".jpg")
    return Response(data={"qrcode":"http://"+BACKEND_DOMIAN+"/media/bind_qr/"+name+".jpg","vtk":name})

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
