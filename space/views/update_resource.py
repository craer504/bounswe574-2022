from django.shortcuts import redirect, render, get_object_or_404
from space.forms import UpdateResourceModelForm
from space.models import ResourceModel, SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def update_resource(request, slug, id):
    resource=get_object_or_404(ResourceModel, id=id)
    form=UpdateResourceModelForm(request.POST or None, files=request.FILES or None, instance=resource)
    if form.is_valid():
        form.save()
        return redirect('spacedetails', slug=slug)    

    return render(request,'pages/update-resource.html', context={'form':form})