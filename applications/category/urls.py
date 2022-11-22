
from django.urls import path
from .views import DetailCategory, ListCategory, GeneratePdf

urlpatterns = [
    path("<uuid:pk>/", DetailCategory.as_view()),
    path("", ListCategory.as_view()),
    path("generate/", GeneratePdf.as_view()),
]
