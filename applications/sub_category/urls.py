from django.urls import path, include
from .views import SubCategoryList, SubCategoryDetail

urlpatterns = [
    path("sub_category/<int:pk>/", SubCategoryDetail.as_view(),
         name="sub_category_detail"),
    path("sub_category/", SubCategoryList.as_view(), name="sub_category_list"),
]
