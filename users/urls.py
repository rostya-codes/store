from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login, UserRegistrationView, UserProfileView, logout  # Controllers

app_name = 'users'  # App name

urlpatterns = [
    path('login/', login, name='login'),  # ../users/login
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('logout', logout, name='logout')
]
