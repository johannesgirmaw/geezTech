
from django.urls import path, include
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category_detail"),
    path("category/", CategoryList.as_view(), name="category_list"),
]
