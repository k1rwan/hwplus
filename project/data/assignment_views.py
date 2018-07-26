from rest_framework import filters, generics

from data import models, permissions, serializers

class HWFAssignmentListView(generics.ListCreateAPIView):
    queryset = models.HWFAssignment.objects.all()
    serializer_class = serializers.HWFAssignmentSerializer

class HWFAssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HWFAssignment.objects.all()
    serializer_class = serializers.HWFAssignmentSerializer

class CourseClassWithAssignments(generics.ListAPIView):
    queryset = models.HWFCourseClass.objects.all()
    serializer_class = serializers.HWFCourseClassSerializerWithAssignments

class CourseClassDetailWithAssignments(generics.RetrieveUpdateAPIView):
    queryset = models.HWFCourseClass.objects.all()
    serializer_class = serializers.HWFCourseClassSerializerWithAssignments