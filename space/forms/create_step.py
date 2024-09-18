from django import forms
from space.models import StepModel, SpaceModel
from django.shortcuts import redirect, render, get_object_or_404


class CreateStepModelForm(forms.ModelForm):
    class Meta:
        model=StepModel
        fields= ('steptitle', 'stepcontent', 'relatedresource')