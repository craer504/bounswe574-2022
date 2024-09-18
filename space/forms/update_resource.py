from django import forms
from space.models import ResourceModel

class UpdateResourceModelForm(forms.ModelForm):
    class Meta:
        model=ResourceModel
        fields= ('resourcename', 'resourceinfo', 'resourceattachment')