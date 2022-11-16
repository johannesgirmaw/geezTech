
from django.urls import path
from .views import DetailCategory, ListCategory, GeneratePdf, SendEmail

urlpatterns = [
    path("<uuid:pk>/", DetailCategory.as_view()),
    path("category/", ListCategory.as_view()),
    path("generate/", GeneratePdf.as_view()),
    path('email/', SendEmail.as_view()),
]
