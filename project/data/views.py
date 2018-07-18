# Create your views here.
from rest_framework import viewsets
from data import models
from data.models import User
from data import serializers
from data import permissions
from project.settings import API_AUTH_KEY, SECRET_KEY
from data.confirm import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from itsdangerous import SignatureExpired
import re

token = Token(SECRET_KEY.encode())
results={
    'SUCCESS':{
        'code':1000,
        'msg':None
    },
    'INACTIVE':{
        'code':4020,
        'msg':'用户未激活'
    },
    'NOT_FOUND':{
        'code':4000,
        'msg':'找不到内容'
    },
    'FORBIDDEN':{
        'code':4030,
        'msg':'您没有权限'
    },
    'EXPIRED':{
        'code':4035,
        'msg':'身份验证过期，请重新登录',
    },
    'REQ_ERR':{
        'code':4040,
        'msg':'参数错误'
    },
    'PWD_ERR':{
        'code':5000,
        'msg':'用户名或密码错误'
    }
}
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

# 登录接口

@api_view(['POST', 'HEAD'])
def login(request):
    global token,data,headers
    try:
        from_username = request.data['username']
        from_password = request.data['password']
    except:
        data['result'] = results['REQ_ERR']
        return Response(data=data,headers=headers)
    try:
        realuser = User.objects.get(bupt_id=from_username)
    except:
        try:
            realuser = User.objects.get(phone=from_username)
        except:
            try:
                realuser = User.objects.get(username=from_username)
            except:
                data['result'] = results['NOT_FOUND']
                return Response(data=data,headers=headers)

    if realuser.check_password(from_password):
        if realuser.is_active==False:
            data['result']=results['INACTIVE']
            return Response(data=data,headers=headers)
        serializer = serializers.UserSerializer(realuser)
        validate_token = token.generate_validate_token(from_username)
        headers['token'] = validate_token
        data['data'] = {key: serializer.data[key]
                        for key in serializer.data if key != 'password'}
        data['result'] = results['SUCCESS']
        return Response(data=data, headers=headers)
    else:
        data['result'] = results['FORBIDDEN']
        return Response(data=data,headers=headers)
    data['result']=results['REQ_ERR']
    return Response(data=data,headers=headers)


@api_view(['GET', 'POST'])
def user_list(request):
    global token,data,headers
    # 用户列表接口
    if request.method == 'GET':
        try:
            # 只有登录了才能看哦
            if token.confirm_validate_token(request.META['HTTP_TOKEN']):
                headers['isLogin'] = True
                headers['authed'] = True
                queryset = User.objects.all()
                try:
                    keywords = request.query_params['keywords']
                    queryset = [obj for obj in queryset if keywords in obj.username or keywords in obj.bupt_id or keywords in obj.name or keywords in obj.email or keywords in obj.phone or keywords in obj.wechat or keywords in obj.class_number]
                except:
                    pass
                serializer = serializers.UserSerializer(queryset, many=True)
                data['data'] = serializer.data
                data['result'] = results['SUCCESS']
                return Response(data=data, headers=headers)
        except SignatureExpired as e:
            print(e)
            data['result']=results['EXPIRED']
            headers['expired']=True
            return Response(headers=headers,data=data)
        else:
            data['result']=results['FORBIDDEN']
            return Response(headers=headers,data=data)
    data = {
        'result': {
            'code':None,
            'msg':None
        },
        'data': None
    }
    headers = {
        'isLogin': False,
        'authed': False
    }
    # 注册接口
    if request.method == 'POST':
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['result'] = results['SUCCESS']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['result'] = {
            'code':5000,
            'msg':str(serializer.errors)
        }
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def user_detail(request, pk):
    global token,data,headers
    try:
        user = User.objects.get(pk=pk)
    except:
        try:
            user = User.objects.get(phone=pk)
        except:
            try:
                user = User.objects.get(bupt_id=pk)
            except:
                data['result']=results['NOT_FOUND']
                return Response(data=data,headers=headers)
    # 获取单个用户信息接口
    # 登录才能看哦
    if request.method == 'GET':
        try:
            token.confirm_validate_token(request.META['HTTP_TOKEN'])
            headers['isLogin'] = True
            headers['authed'] = True
            serializer = serializers.UserSerializer(user)
            data['data'] = serializer.data
            data['result'] = results['SUCCESS']
            return Response(data=data, headers=headers)
        except SignatureExpired as e:
            print(e)
            data['result']=results['EXPIRED']
            headers['expired']=True
            return Response(headers=headers,data=data)
        else:
            data['result']=results['FORBIDDEN']
            return Response(data=data, headers=headers)
    # 修改用户信息接口
    # 只有自己才能改哦
    elif request.method == 'PUT':
        try:
            plain = token.confirm_validate_token(request.META['HTTP_TOKEN'])
            try:
                found_user = User.objects.get(bupt_id=plain)
            except:
                try:
                    found_user = User.objects.get(phone=plain)
                except:
                    try:
                        found_user = User.objects.get(username=plain)
                    except:
                        data['result']=results['NOT_FOUND']
                        return Response(data=data, headers=headers)
        except SignatureExpired as e:
            print(e)
            data['result']=results['EXPIRED']
            headers['expired']=True
            return Response(headers=headers,data=data)
        else:
            data['result']=results['FORBIDDEN']
            return Response(data=data, headers=headers)

        headers['isLogin'] = True
        if found_user == request.user:
            headers['authed'] = True
            serializer = serializers.UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data['data'] = serializer.data
                data['result'] = results['SUCCESS']
                return Response(data=data, headers=headers)
            else:
                data['result']=results['REQ_ERR']
                return Response(data=data, headers=headers)
        else:
            data['result']=results['FORBIDDEN']
            return Response(data=data, headers=headers)

@api_view(['POST'])
def is_repeated(request):
    to_judge=request.data['content']
    all_data=User.objects.values_list(request.data['type']).all()
    all_data=[item[0] for item in all_data]
    data['data']={"repeat":(to_judge in all_data)}
    return Response(data=data,headers=headers)

# 激活账户
@api_view(['POST'])
def activate(request):
    global data,headers,token
    usrn=token.confirm_validate_token(request.META['HTTP_TOKEN'])
    if usrn:
        user_obj=User.objects.get(username=usrn)
        user_obj.is_active=True
        user_obj.save()
    return Response(data=data,headers=headers)

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
