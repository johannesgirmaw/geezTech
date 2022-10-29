
from django.urls import path
from .views import DetailCategory, ListCategory

urlpatterns = [
    path("<uuid:pk>/",DetailCategory.as_view()),
    path("",ListCategory.as_view())
]