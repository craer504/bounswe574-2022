from django.shortcuts import redirect, render, get_object_or_404
from space.forms import CreateContentForm
from space.models import ContentModel, RelationModel, SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required
def delete_content(request, id,slug):
    # OrderSparePart is the Model of which the object is present

    ob = ContentModel.objects.get(id=id)
    ob.delete()
    return redirect('display-contents',slug=slug) 