from django.shortcuts import render, get_object_or_404
from space.models import SpaceModel, StepModel, ResourceModel


def display_step(request, slug,id): 
    space=get_object_or_404(SpaceModel, slug=slug)
    step=get_object_or_404(StepModel,id=id)
    steps=space.steps.all()    
    resources=space.resources.all()

    return render(request,'pages/display-step.html', context={
        'space':space,
        'steps':steps,
        'step':step,
        'resources':resources,
    })