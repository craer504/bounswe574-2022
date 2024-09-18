
from django.shortcuts import redirect, render, get_object_or_404
from space.forms import CreateContentForm
from space.models import ContentModel, RelationModel, SpaceModel
from django.contrib.auth.decorators  import login_required
from django.http import JsonResponse
from django.core import serializers

@login_required
def content_relations(request, slug):
    current_space = get_object_or_404(SpaceModel, slug=slug)
    nodes = list(ContentModel.objects.filter(space_id=current_space.id).values())
    relations = list(RelationModel.objects.filter(space_id=current_space.id).values())
    #json_relations = serializers.serialize('json', [ relations ])
    return JsonResponse({"nodes": nodes, "relations":relations}, status=200)

