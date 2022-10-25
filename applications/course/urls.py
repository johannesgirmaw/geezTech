
from django.urls import path
from .views import CourseListCreateView, CourseDetail

urlpatterns = [
    path("course/", CourseListCreateView.as_view(), name="course_list_create"),
    path("course/<uuid:pk>/update", CourseDetail.as_view(),
         name="course_Update"),

    #     path("course/<uuid:pk>/retrieve", CourseDetailRetrieveView.as_view(),
    #          name="course_retrieve"),
    #     path("course/<uuid:pk>/delete", CourseDetailDestroyView.as_view(),
    #          name="course_destroy"),
]
