from django.shortcuts import redirect, render, get_object_or_404
from space.models import SpaceModel, ResourceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def delete_resource(request, slug, id):
    #space=get_object_or_404(SpaceModel, slug=slug)
    #get_object_or_404(ResourceModel, resourcespace=space, resourcecreator=request.user).delete()

    rm = ResourceModel.objects.get(id=id)
    rm.delete()
    return redirect('spacedetails', slug=slug)    
