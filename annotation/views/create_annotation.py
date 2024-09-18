from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from annotation.models import  AnnotationModel


@login_required(login_url='/')
@csrf_exempt
def create_annotation(request):
    if  request.method == "POST":
        ann = AnnotationModel()
        ann.annotation = request.POST.get('annotation')
        ann.save()

        return JsonResponse({"data": 'success'}, status=200)

    return JsonResponse({"error": "Please try again later"}, status=400)