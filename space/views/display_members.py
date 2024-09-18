from django.shortcuts import render, get_object_or_404
from space.models import SpaceModel, ResourceModel, StepModel, ExtendedUser
from django.contrib.auth.models import User


def display_members(request, slug,id): 
    space=get_object_or_404(SpaceModel, slug=slug)
    member=get_object_or_404(ExtendedUser, extendeduser=id)
    member1=get_object_or_404(User, id=id)
    members=space.members.all()

    return render(request,'pages/display-members.html', context={
        'space':space,
        'member':member,
        'members':members,
        'member1':member1
    })