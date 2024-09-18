from django.shortcuts import render

def warning(request):
    context={'spacewarn':'You have send your message into wrong space, please select right space and try it again.'}
    return render(request,'pages/warning.html', context=context)