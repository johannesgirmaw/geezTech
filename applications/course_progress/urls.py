
from django.urls import path
from .views import ChapterProgressDetail, ChapterProgressListCreateView, ContentProgressDetail, ContentProgressListCreateView, CourseProgressDetail, CourseProgressListCreateView

urlpatterns = [
    path("course/<uuid:pk>/", CourseProgressDetail.as_view(),
         name="course_progress_detail"),
    path("course/", CourseProgressListCreateView.as_view(),
         name="course_progress_list_create"),
    path("chapter/<uuid:pk>/", ChapterProgressDetail.as_view(),
         name="chapter_progress_detail"),
    path("chapter/", ChapterProgressListCreateView.as_view(),
         name="chapter_progress_list_create"),
    path("content/<uuid:pk>/", ContentProgressDetail.as_view(),
         name="content_progress_detail"),
    path("content/", ContentProgressListCreateView.as_view(),
         name="content_progress_list_create"),
]
