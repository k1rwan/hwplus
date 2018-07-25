from rest_framework import filters, generics

from data import models, permissions, serializers

class HWFAssignmentListView(generics.ListCreateAPIView):
    queryset = models.HWFAssignment.objects.all()
    serializer_class = serializers.HWFAssignmentSerializer

class HWFAssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HWFAssignment.objects.all()
    serializer_class = serializers.HWFAssignmentSerializer

