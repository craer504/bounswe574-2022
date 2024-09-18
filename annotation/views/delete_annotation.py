from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from annotation.models import  AnnotationModel
import json

@login_required(login_url='/')
@csrf_exempt
def delete_annotation(request):
    if  request.method == "POST":
        annotation= json.loads(request.POST.get('annotation'))
        ann = AnnotationModel.objects.get(annotation__0__icontains=annotation["id"])
        annotationJson = json.loads(ann.annotation)
        if annotationJson["body"][0]["creator"]["name"] == request.user.username:
            ann.delete()
            return JsonResponse({"data": 'success'}, status=200)
        return JsonResponse({"error": "Unauthorized"}, status = 403)

    return JsonResponse({"error": "Please try again later"}, status=400)