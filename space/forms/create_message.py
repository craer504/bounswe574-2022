from django import forms
from space.models import MessageModel

class CreateMessageModelForm(forms.ModelForm):
    class Meta:
        model=MessageModel
        fields= ('message',)