from django.urls import path 
from .views import FeedbacksDetail, FeedbacksListCreateView

urlpatterns = [
    path('',FeedbacksListCreateView.as_view(), name = 'feedback-list'),
    path('<uuid:pk>/', FeedbacksDetail.as_view(), name = 'feedback-detail')
]

