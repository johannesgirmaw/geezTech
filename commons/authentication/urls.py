
from django.urls import path,include
from .views import CustomRegisterView,ListUser,DetailUser
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularRedocView,
SpectacularSwaggerView, # new
)

urlpatterns = [
    path("registration/",CustomRegisterView.as_view()),
    path("users/",ListUser.as_view()),
    path('users/<uuid:pk>/',DetailUser.as_view()),
    path('authorize/', include('dj_rest_auth.urls')),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
