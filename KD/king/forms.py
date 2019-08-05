from django import forms
from django.core import validators
from king.models import Customers, UserProfileInfo
from django.contrib.auth.models import User


class NewUser(forms.ModelForm):
    class Meta():
        model = Customers
        fields = '__all__'

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('phone_number','profile_picture', 'address')
