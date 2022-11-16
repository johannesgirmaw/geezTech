
from django.urls import path, include

urlpatterns = [
    path('', include("applications.course.urls")),
    path('', include("applications.category.urls")),
    path('', include("applications.chapters.urls")),
]
