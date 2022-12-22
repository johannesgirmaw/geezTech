
from django.urls import path
from .views import DetailCategory, ListCategory, GeneratePdf

urlpatterns = [
    path("<uuid:pk>/", DetailCategory.as_view(), name="category-detail"),
    path("", ListCategory.as_view()),
    path("generate/", GeneratePdf.as_view()),
]
