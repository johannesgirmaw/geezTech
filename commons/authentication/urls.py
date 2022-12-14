
from django.urls import path,include,re_path
from .views import CustomRegisterView,ListUser, CustomUserManager, ListGroup, DetailGroup,ListUserPermission,ListEducationalBackground,DetailEducationalBackground, UserDetail
from rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView
from commons.utils.regex_utils import token_regex, uuid_regex , key_regex 

urlpatterns = [
    path("registration/",CustomRegisterView.as_view()),
    path("users/",ListUser.as_view()),
    path('users/<uuid:pk>/',UserDetail.as_view()),
    path("groups/", ListGroup().as_view()),
    path("user_permissions/",ListUserPermission.as_view()),
    path("create_manager/", CustomUserManager.as_view()),
    path("authorize/user/educational_background/",ListEducationalBackground.as_view(), name = "list-educational-background"),
    path("authorize/user/educational_background/<uuid:pk>/",DetailEducationalBackground.as_view(), name = "detail-educational-background"),
    path('authorize/', include('dj_rest_auth.urls')),
    re_path(r'^authorize/password/reset/confirm/(?P<uidb64>' + uuid_regex + ')/(?P<token>' + token_regex + ')/$',PasswordResetConfirmView.as_view(),name='password_reset_confirm'), 
    re_path(r'^account-confirm-email/(?P<key>'+ key_regex +')$', VerifyEmailView.as_view(),name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
            name='account_email_verification_sent')
]
