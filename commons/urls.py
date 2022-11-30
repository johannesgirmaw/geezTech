
from django.urls import path, include

urlpatterns = [
    path('',include("commons.authentication.urls")),
    path("message/", include("commons.message_util.urls"), name = "message"),
    path("feedback/", include("commons.feedback.urls"), name = "feedback"),
]
