from django.shortcuts import render, get_object_or_404
from space.models import SpaceModel, ResourceModel


def display_resource(request, slug,id): 
    space=get_object_or_404(SpaceModel, slug=slug)
    resource=get_object_or_404(ResourceModel,id=id)

    return render(request,'pages/display-resource-2.html', context={
        'space':space,
        'resource':resource,
    })