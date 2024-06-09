from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    """ User login form """
    class Meta:
        model = User
        fields = ('username', 'password')
