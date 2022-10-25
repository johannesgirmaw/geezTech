
from django.urls import path,include
from .views import CustomRegisterView,ListUser,DetailUser

urlpatterns = [
    path("registration/",CustomRegisterView.as_view()),
    path("users/",ListUser.as_view()),
    path('users/<uuid:pk>/',DetailUser.as_view()),
    path('authorize/', include('dj_rest_auth.urls')),
]
