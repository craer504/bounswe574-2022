from django.shortcuts import redirect, render
from space.forms import SpaceModelForm
from space.models import SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def spaces(request):
    form=SpaceModelForm()
    if form.is_valid():
        space=form.save(commit=False)
        space.author=request.user
        space.save()
        form.save_m2m
        return redirect('spacedetails', slug=space.slug)    

    return render(request,'pages/spaces.html', context={'form':form})