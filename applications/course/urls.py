
from django.urls import path
from .views import CourseListCreateView, CourseDetail, CourseCartListCreateView, EnrollementListCreateView, EnrollementDetail

urlpatterns = [
    path("", CourseListCreateView.as_view(), name="course_list_create"),
    path("<uuid:pk>/update", CourseDetail.as_view(),
         name="course_Update"),
    path("cart/", CourseCartListCreateView.as_view(),
         name="course_cart"),
    path("enroll/", EnrollementListCreateView.as_view(), name="course_enroll"),
    path("enroll/<uuid:id>", EnrollementDetail.as_view(),
         name="course_enroll_detail"),
]
