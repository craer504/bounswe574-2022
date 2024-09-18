from django import forms
from space.models import SpaceModel

class CreateSpaceModelForm(forms.ModelForm):
    class Meta:
        model=SpaceModel
        fields= ('title', 'content', 'members')