from django.contrib.auth import logout
from django.shortcuts import redirect, render

def signout(request):
    logout(request)
    return redirect('homepage')