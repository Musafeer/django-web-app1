from django import forms
from helloworld.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    passwords = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('occupation', 'company', 'hobby')