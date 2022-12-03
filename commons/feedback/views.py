from .models import Feedbacks
from .serializers import FeedbacksSerializer
from rest_framework import generics, filters
from commons.utils.permissions import CustomPermission
# from django.db.models import F


class FeedbacksListCreateView(generics.ListCreateAPIView):
    # permission_classes = [CustomPermission]
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['feedback', 'user__first_name','user__middle_name','user__last_name']
    ordering_fields  = ['feedback', 'user__first_name','user__middle_name','user__last_name']
    ordering = '-create_date'
    # def get_queryset(self):
    #     queryset = Feedbacks.objects.filter(user__middle_name = F('user__last_name'))
    #     return queryset
    

class FeedbacksDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer