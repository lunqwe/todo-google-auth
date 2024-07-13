from django.urls import path, re_path
from dj_rest_auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from .views import CreateUserView, LoginUserView, UserView, GoogleLoginView



urlpatterns = [
    path('register/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('user/<int:pk>/', UserView.as_view(), name='get_user'),
    path('google-auth/', GoogleLoginView.as_view(), name='google_login'),
    path('password-reset/',PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
