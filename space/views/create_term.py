from django.shortcuts import redirect, render, get_object_or_404
from space.models import SpaceModel
from space.forms import CreateTermModelForm, CreateSpaceModelForm

def create_term(request, slug):
    space=get_object_or_404(SpaceModel, slug=slug)
    form=CreateTermModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        term=form.save(commit=False)
        term.termwriter=request.user
        term.termspace=space
        term.save()
        
        return redirect('spacedetails', slug= term.termspace.slug)    

    return render(request,'pages/create-term.html', context={'form':form, 'space':space})