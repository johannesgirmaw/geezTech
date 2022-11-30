
from django.urls import path
from .views import ChapterProgressDetail, ChapterProgressListCreateView, ContentProgressDetail, ContentProgressListCreateView, CourseProgressDetail, CourseProgressListCreateView

urlpatterns = [
    path("course/<uuid:pk>/", CourseProgressDetail.as_view()),
    path("course/", CourseProgressListCreateView.as_view()),
    path("chapter/<uuid:pk>/", ChapterProgressDetail.as_view()),
    path("chapter/", ChapterProgressListCreateView.as_view()),
    path("content/<uuid:pk>/", ContentProgressDetail.as_view()),
    path("content/", ContentProgressListCreateView.as_view()),
]
