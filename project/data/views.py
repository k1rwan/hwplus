# Create your views here.
import re

import qrcode
from itsdangerous import SignatureExpired
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from data import models, permissions, serializers
from data.confirm import ShortToken, Token, send
from data.models import User
from project.settings import API_AUTH_KEY, SECRET_KEY

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
    qr = qrcode.make(request.data['content'])
    qr.save("./data/backend_media/invitation_qr/ppp.jpg")
    return Response(data={"qrcode":"http://localhost:8000/media/invitation_qr/ppp.jpg"})


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
