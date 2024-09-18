from django.shortcuts import redirect, render
from django.contrib.auth.decorators  import login_required
from django.contrib import messages
from space.forms import EditProfile1Form
from space.models import ExtendedUser

@login_required(login_url='/')
def edit_profile1(request):
        
    if request.method== 'POST':
        form = EditProfile1Form(request.POST, request.FILES, instance=request.user)          
        if form.is_valid():           
            newuser=ExtendedUser.objects.get(extendeduser=request.user.id) 
            newuser.interest = form.cleaned_data['InterestArea']
            newuser.save()
            form.save()                        
            messages.success(request, 'Profile has been successfully updated.')
    else:
        form=EditProfile1Form(instance=request.user)     

    return render(request,'pages/edit-profile1.html', context={'form':form})