
from django.urls import path, include

urlpatterns = [
    path('',include("applications.course.urls")),
    path("category/", include("applications.category.urls")),
]
