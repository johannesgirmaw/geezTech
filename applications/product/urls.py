
from django.urls import path, include
from .views import SubCategoryList, SubCategoryDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("product/<int:pk>/", SubCategoryDetail.as_view(),
         name="product_detail"),
    path("product/", SubCategoryList.as_view(), name="product_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
