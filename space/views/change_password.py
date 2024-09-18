from django.shortcuts import redirect, render
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/')
def change_password(request):
    if request.method== 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            platformuser=form.save()
            update_session_auth_hash(request, platformuser)
            messages.success(request, 'Password has beeen successfully changed.')
            return redirect('change-password')
    else:
        form=PasswordChangeForm(request.user)

    return render(request,'pages/change-password.html', context={'form':form})