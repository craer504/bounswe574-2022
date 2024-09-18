from django.shortcuts import redirect, render, get_object_or_404
from space.forms import CreateMessageModelForm, CreateSpaceModelForm
from space.models import SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def create_message(request, slug):
    space=get_object_or_404(SpaceModel, slug=slug)
    form=CreateMessageModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        message=form.save(commit=False)
        message.sender=request.user
        message.memberspace=space
        message.save()
        
        return redirect('spacedetails', slug= message.memberspace.slug)    

    return render(request,'pages/create-message.html', context={'form':form, 'space':space})