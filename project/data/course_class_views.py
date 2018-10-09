# Reserve in case

from project.settings import FRONTEND_DOMAIN, BACKEND_DOMIAN
from data.views import short_token,token
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import qrcode

from data import models, permissions, serializers

# RESTful API for HWFCourseClass

# class HWFCourseClassListView(generics.ListCreateAPIView):

#     queryset = models.HWFCourseClass.objects.all()
#     serializer_class = serializers.HWFCourseClassSerializer
#     permission_classes = (
#         permissions.SelfEditTeacherAppendUserReadForHWFCourseClass,)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('name', 'description')

#     def perform_create(self, serializer):
#         user_token = self.request.META['HTTP_TOKEN']
#         realuser = models.User.objects.get(username=token.confirm_validate_token(user_token))
#         serializer.save(teachers=[realuser])



# class HWFCourseClassDetailView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = models.HWFCourseClass.objects.all()
#     serializer_class = serializers.HWFCourseClassSerializer
#     permission_classes = (
#         permissions.SelfEditTeacherAppendUserReadForHWFCourseClass,)


# class UserWithCourseListViewForStudent(generics.ListAPIView):

#     queryset = models.User.objects.filter(usertype='student')
#     serializer_class = serializers.UserSerializerCourseForStudent
#     permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


# class UserWithCourseDetailViewForStudent(generics.RetrieveUpdateAPIView):

#     queryset = models.User.objects.filter(usertype='student')
#     serializer_class = serializers.UserSerializerCourseForStudent
#     # permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


# class UserWithCourseListViewForTeacher(generics.ListAPIView):

#     queryset = models.User.objects.filter(usertype='teacher')
#     serializer_class = serializers.UserSerializerCourseForTeacher
#     permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


# class UserWithCourseDetailViewForTeacher(generics.RetrieveUpdateAPIView):

#     queryset = models.User.objects.filter(usertype='teacher')
#     serializer_class = serializers.UserSerializerCourseForTeacher
#     permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


# class UserWithCourseListViewForAssistant(generics.ListAPIView):

#     queryset = models.User.objects.filter(usertype='assistant')
#     serializer_class = serializers.UserSerializerCourseForAssistant
#     permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


# class UserWithCourseDetailViewForAssistant(generics.RetrieveUpdateAPIView):

#     queryset = models.User.objects.filter(usertype='assistant')
#     serializer_class = serializers.UserSerializerCourseForAssistant
#     permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)
