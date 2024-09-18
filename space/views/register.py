from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from space.models import ExtendedUser

def register(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password1')
           user=User.objects.create_user(username=username, password=password)
           user.save()
           ExtendedUser.objects.create(extendeduser_id=user.id)           
           user=authenticate(username=username, password=password)
           login (request, user)
           messages.success(request, 'You have been successfully registered.')
           return redirect('homepage')
    else:
        form=UserCreationForm()

    return render(request,'pages/register.html', context={'form':form})

