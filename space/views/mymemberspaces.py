from django.shortcuts import render
from space.models import SpaceModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def mymemberspaces(request): 

    allspaces=request.user.includedSpaces.order_by('-id')

    page=request.GET.get('page')
    paginator=Paginator(allspaces,3)

    return render(request,'pages/mymemberspaces.html', context={'allspaces':paginator.get_page(page)})
