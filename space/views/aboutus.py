from django.shortcuts import render

def aboutus(request):
    return render(request,'pages/aboutus.html', context={})