
from django.urls import path,include,re_path
from .views import CustomRegisterView,ListUser,DetailUser
from rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path("registration/",CustomRegisterView.as_view()),
    path("users/",ListUser.as_view()),
    path('users/<uuid:pk>/',DetailUser.as_view()),
    path('authorize/', include('dj_rest_auth.urls')),
    re_path(r'^authorize/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,6}-[0-9A-Za-z]{1,32})/$',PasswordResetConfirmView.as_view(),name='password_reset_confirm'), re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
            name='account_email_verification_sent')
]
