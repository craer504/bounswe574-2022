
from django.shortcuts import redirect, render, get_object_or_404
from space.forms import CreateContentForm
from space.models import ContentModel, RelationModel, SpaceModel
from django.contrib.auth.decorators  import login_required


@login_required
def display_contents(request, slug):
    current_space = get_object_or_404(SpaceModel, slug=slug)
    contents = list(ContentModel.objects.filter(space_id=current_space.id).values())
    context = {'contents': contents, 'space':current_space}
    return render(request, 'pages/display-contents.html', context)

