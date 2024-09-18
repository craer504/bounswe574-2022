from django.shortcuts import render
from space.models import SpaceModel, ExtendedUser
from django.core.paginator import Paginator
from django.db.models import Q



def homepage(request): 
    search=request.GET.get('search')

    users=ExtendedUser.objects.order_by('-id')
    allspaces=SpaceModel.objects.order_by('-id')
    if search:
        allspaces= allspaces.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search) |
            Q(searchwords__icontains=search) |
            Q(tag1__icontains=search) |
            Q(tag2__icontains=search) |
            Q(tag3__icontains=search) 
        ).distinct()
        
    page=request.GET.get('page')
    paginator=Paginator(allspaces,3)

    return render(request,'pages/homepage.html', context={'allspaces':paginator.get_page(page),'users':users})
