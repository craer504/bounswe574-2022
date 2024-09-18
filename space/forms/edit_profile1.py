from django import forms
from space.models import ExtendedUser
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserModel

class EditProfile1Form(forms.Form, UserChangeForm):
    password= None
    class Meta:
        model=UserModel()
        fields={'last_name','first_name','email','username'}
    
    InterestArea=forms.CharField()