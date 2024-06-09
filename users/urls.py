from django.urls import path

from users.views import login, registration  # Controllers

app_name = 'users'  # App name

urlpatterns = [
    path('login/', login, name='login'),  # ../users/login
    path('registration/', registration, name='registration')  # ../users/registration
]
