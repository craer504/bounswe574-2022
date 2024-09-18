from django.conf import settings
from django.http.response import HttpResponseForbidden, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse

import django_filters
from rest_framework import status, viewsets
from rest_framework.response import Response

import annotator
from annotator import filters, models
from annotator.serializers import AnnotationGetSerializer,AnnotationPostSerializer



class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = models.Annotation.objects.all()
    #serializer_class = serializers.AnnotationSerializer
    #filter_class = filters.AnnotationFilterSet
    #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['uri']
    
    def root(self, _):

        return JsonResponse(
            {
                "name": getattr(settings, "ANNOTATOR_NAME", "django-annotator-store"),
                "version": annotator.__version__,
            }
        )

    def search(self, _):

        queryset = super(AnnotationViewSet, self).filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({"total": len(serializer.data), "rows": serializer.data})

    def get_success_headers(self, data):

        headers = super(AnnotationViewSet, self).get_success_headers(data)

        url = reverse("annotations-detail", kwargs={"pk": data["id"]})
        headers.update({"Location": self.request.build_absolute_uri(url)})

        return headers

    
    def create(self, request, *args, **kwargs):

        response = super(AnnotationViewSet, self).create(request, *args, **kwargs)
        response.data = None
        response.status_code = status.HTTP_303_SEE_OTHER
        return response

    def update(self, request, *args, **kwargs):

        response = super(AnnotationViewSet, self).update(request, *args, **kwargs)
        for h, v in self.get_success_headers(response.data).items():
            response[h] = v
        response.data = None
        response.status_code = status.HTTP_303_SEE_OTHER
        return response
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return AnnotationPostSerializer
        return AnnotationGetSerializer

