from django.urls import path
from .views import ListQuestions,DetailQuestions, OptionsOfQuestions,ListOptions,ListAnswers,DetailAnswers,DetailOptions

urlpatterns = [
    path("<uuid:pk>/", DetailQuestions.as_view(), name='questions-detail'),
    # path('<uuid:id>/options/', OptionsOfQuestions.as_view()),
    path("", ListQuestions.as_view()),
    path("options/<uuid:id>/", DetailOptions.as_view()),    
    path("options/", ListOptions.as_view()),
    path("answer/<uuid:id>/", ListAnswers.as_view(), name= 'answers_detail'),
    path("answer/", DetailAnswers.as_view(),name='answers_list'),
]
