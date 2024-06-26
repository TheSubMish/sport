from django import forms
from .models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'country',
            'fav_sport',
            'password',
        ]