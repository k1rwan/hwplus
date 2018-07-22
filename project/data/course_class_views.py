# Create your views here.
from rest_framework import filters, generics, viewsets

from data import models, permissions, serializers


class HWFCourseClassListView(generics.ListCreateAPIView):

    queryset = models.HWFCourseClass.objects.all()
    serializer_class = serializers.HWFCourseClassSerializer
    permission_classes = (
        permissions.SelfEditTeacherAppendUserReadForHWFCourseClass,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')

    def get_queryset(self):
        crtr = self.request.query_params.get('creator', None)
        if crtr != None:
            crtr_id = int(crtr)
            return models.HWFCourseClass.objects.filter(creator_id=crtr_id)
        else:
            return models.HWFCourseClass.objects.all()


class HWFCourseClassDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.HWFCourseClass.objects.all()
    serializer_class = serializers.HWFCourseClassSerializer
    permission_classes = (
        permissions.SelfEditTeacherAppendUserReadForHWFCourseClass,)


class UserWithCourseListViewForStudent(generics.ListAPIView):

    queryset = models.User.objects.filter(usertype='student')
    serializer_class = serializers.UserSerializerCourseForStudent
    permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


class UserWithCourseDetailViewForStudent(generics.RetrieveUpdateAPIView):

    queryset = models.User.objects.filter(usertype='student')
    serializer_class = serializers.UserSerializerCourseForStudent
    permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


class UserWithCourseListViewForTeacher(generics.ListAPIView):

    queryset = models.User.objects.filter(usertype='teacher')
    serializer_class = serializers.UserSerializerCourseForTeacher
    permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


class UserWithCourseDetailViewForTeacher(generics.RetrieveUpdateAPIView):

    queryset = models.User.objects.filter(usertype='teacher')
    serializer_class = serializers.UserSerializerCourseForTeacher
    permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


class UserWithCourseListViewForAssistant(generics.ListAPIView):

    queryset = models.User.objects.filter(usertype='assistant')
    serializer_class = serializers.UserSerializerCourseForAssistant
    permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)


class UserWithCourseDetailViewForAssistant(generics.RetrieveUpdateAPIView):

    queryset = models.User.objects.filter(usertype='assistant')
    serializer_class = serializers.UserSerializerCourseForAssistant
    permission_classes = (permissions.SelfEditUserReadForHWFCourseClass,)
