from django.shortcuts import redirect, render, get_object_or_404
from space.models import SpaceModel
from space.forms import CreateStepModelForm, CreateSpaceModelForm

def create_step(request, slug):
    space=get_object_or_404(SpaceModel, slug=slug)
    form=CreateStepModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        step=form.save(commit=False)
        step.stepcreator=request.user
        step.stepspace=space
        step.save()
        
        return redirect('spacedetails', slug= step.stepspace.slug)    

    return render(request,'pages/create-step.html', context={'form':form, 'space':space})