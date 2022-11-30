
from django.urls import path, include

urlpatterns = [
    path('course/', include("applications.course.urls")),
    path("category/", include("applications.category.urls")),
    path('chapters/', include("applications.chapters.urls")),
    path('', include("applications.content.urls")),
    path('questions/', include('applications.assignment.urls')),
    path('progress/', include('applications.course_progress.urls'))

]
