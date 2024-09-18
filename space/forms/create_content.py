from django import forms
from space.models import ContentModel 

class CreateContentForm(forms.ModelForm):
    class Meta:
        model = ContentModel
        fields= ('title','link')