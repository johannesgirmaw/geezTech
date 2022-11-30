
from django.urls import path
from .views import DetailChapter, ListChapter

urlpatterns = [
    path("<uuid:pk>/", DetailChapter.as_view(), name = 'chapter-detail'),
    path("", ListChapter.as_view(), name = 'chapter-list'),
]
