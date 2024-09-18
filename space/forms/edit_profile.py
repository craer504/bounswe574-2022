from dataclasses import field
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserModel

class EditProfileForm(UserChangeForm):
    password= None
    class Meta:
        model=UserModel()
        fields={'email', 'first_name', 'last_name'}