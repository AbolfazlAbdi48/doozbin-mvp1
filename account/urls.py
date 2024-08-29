from django.urls import path
from .views import (
    login_view,
    verify_otp_view,
    complete_register_view,
    user_profile_view,
    UserAssetListView
)

app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('login/verify/', verify_otp_view, name='otp-verify'),
    path('login/register/', complete_register_view, name='complete-register'),
    path('profile/', user_profile_view, name='user-profile'),
    path('profile/assets/', UserAssetListView.as_view(), name='user-asset'),
]
