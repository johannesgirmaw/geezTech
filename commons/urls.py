
from django.urls import path, include

urlpatterns = [
    path('',include("commons.authentication.urls"))
]
