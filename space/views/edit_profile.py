from django.shortcuts import redirect, render
from django.contrib.auth.decorators  import login_required
from django.contrib import messages
from space.forms import EditProfileForm

@login_required(login_url='/')
def edit_profile(request):
    if request.method== 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
           form.save()
           messages.success(request, 'Profile has been successfully updated.')
    else:
        form=EditProfileForm(instance=request.user)

    return render(request,'pages/edit-profile.html', context={'form':form})