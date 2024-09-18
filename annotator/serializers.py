from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from annotator import models


class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Range
        exclude = ("annotation", "id")


class AnnotationPostSerializer(WritableNestedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ranges = RangeSerializer(many=True)

    class Meta:
        model = models.Annotation
        fields = "__all__"



class AnnotationGetSerializer(WritableNestedModelSerializer):
    user = serializers.CharField(default=serializers.CurrentUserDefault())
    ranges = RangeSerializer(many=True)

    class Meta:
        model = models.Annotation
        fields = "__all__"

