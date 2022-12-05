
from django.urls import path
from .views import DetailChapter, ListChapter

urlpatterns = [
    path("", ListChapter.as_view(), name="chapter_list_create"),
    path("<uuid:pk>/", DetailChapter.as_view(), name='chapter_detail'),
]
