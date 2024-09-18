from django.shortcuts import redirect, render, get_object_or_404
from space.models import SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def delete_space(request, slug):
    get_object_or_404(SpaceModel, slug=slug, author=request.user).delete()
    return redirect('mycreatedspaces')    
