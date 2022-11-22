
from django.urls import path
from .views import CourseListCreateView, CourseDetail, CourseCartListCreateView, EnrollementListCreateView, EnrollementDetail, CoursePriceListCreateView, CoursePriceDetail, ReviewerDetail, ReviewerListCreateView

urlpatterns = [
    path("", CourseListCreateView.as_view(), name="course_list_create"),
    path("<uuid:pk>/update", CourseDetail.as_view(),
         name="course_Update"),
    path("cart/", CourseCartListCreateView.as_view(),
         name="course_cart"),
    path("enroll/", EnrollementListCreateView.as_view(), name="course_enroll"),
    path("enroll/<uuid:id>", EnrollementDetail.as_view(),
         name="course_enroll_detail"),

    path("review/", ReviewerListCreateView.as_view(), name="course_review"),
    path("review/<uuid:id>", ReviewerDetail.as_view(),
         name="course_review_detail"),

    path("price/", CoursePriceListCreateView.as_view(), name="course_price"),
    path("price/<uuid:id>", CoursePriceDetail.as_view(),
         name="course_price_detail"),
]
