
from django.urls import path
from .views import ContentListCreateView, ContentDetail

urlpatterns = [
    path("", ContentListCreateView.as_view(), name="content_list_create"),
    path("<uuid:pk>/", ContentDetail.as_view(),
         name="content_Update"),
]
