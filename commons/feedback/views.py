from .models import Feedbacks
from .serializers import FeedbacksSerializer
from rest_framework import generics, filters
from commons.permission.permissions import CustomPermission


class FeedbacksListCreateView(generics.ListCreateAPIView):
    # permission_classes = [CustomPermission]
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['feedback', 'user__first_name','user__middle_name','user__last_name']


class FeedbacksDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer