from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from annotation.models import  AnnotationModel
import json


@login_required(login_url='/')
@csrf_exempt
def get_annotations(request):
    if  request.method == "GET":
        res = []
        data = list(AnnotationModel.objects.filter(annotation__0__icontains=request.GET.get('uri')).values_list('annotation'))
        print(len(data))
        for ann in data:
            print(ann)
            json_data =json.loads(ann[0])
            res.append(json_data)

        return JsonResponse(res, safe=False)


    return JsonResponse({"error": "Please try again later"}, status=400)