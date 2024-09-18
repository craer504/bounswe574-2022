from django.shortcuts import redirect, render, get_object_or_404
from space.models import SpaceModel
from space.forms import ResourceModelForm

def resource(request, slug):
    space=get_object_or_404(SpaceModel, slug=slug)
    form=ResourceModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        resource=form.save(commit=False)
        resource.resourcecreator=request.user
        resource.resourcespace=space
        resource.save()
        
        return redirect('spacedetails', slug= resource.resourcespace.slug)    

    return render(request,'pages/resource.html', context={'form':form, 'space':space})