from django.urls import path
from .views import ListQuestions,DetailQuestions, OptionsOfQuestions,ListOptions,ListAnswers,DetailAnswers,DetailOptions, DetailCertificates, ListCertificates

urlpatterns = [
    path("<uuid:pk>/", DetailQuestions.as_view(), name='questions-detail'),
    # path('<uuid:id>/options/', OptionsOfQuestions.as_view()),
    path("", ListQuestions.as_view()),
    path("options/<uuid:id>/", DetailOptions.as_view()),    
    path("options/", ListOptions.as_view()),
    path("answer/<uuid:id>/", ListAnswers.as_view(), name= 'answers_detail'),
    path("answer/", DetailAnswers.as_view(),name='answers_list'),
    path("certificate/", ListCertificates.as_view(), name = 'certificate-list'),
    path('certificate/<uuid:pk>/', DetailCertificates.as_view(), name = 'certificate-detail')
]
