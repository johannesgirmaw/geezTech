
from django.urls import path
from .views import ContentListCreateView, ContentDetail

urlpatterns = [
    path("content/", ContentListCreateView.as_view(), name="content_list_create"),
    path("content/<uuid:pk>/update", ContentDetail.as_view(),
         name="content_Update"),
]
