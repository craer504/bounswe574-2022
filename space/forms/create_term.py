from django import forms
from space.models import TermModel

class CreateTermModelForm(forms.ModelForm):
    class Meta:
        model=TermModel
        fields= ('termtitle', 'termdefinition', 'termstep')