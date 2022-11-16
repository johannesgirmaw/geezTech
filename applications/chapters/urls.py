
from django.urls import path
from .views import DetailChapter, ListChapter

urlpatterns = [
    path("<uuid:pk>/", DetailChapter.as_view()),
    path("chapters/", ListChapter.as_view()),
]
