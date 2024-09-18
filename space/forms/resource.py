from django import forms
from space.models import ResourceModel

class ResourceModelForm(forms.ModelForm):
    class Meta:
        model=ResourceModel
        fields= ('resourcename', 'resourceinfo', 'resourceattachment')