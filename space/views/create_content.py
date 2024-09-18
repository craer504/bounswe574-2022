
from django.shortcuts import redirect, render, get_object_or_404
from space.forms import CreateContentForm
from space.models import ContentModel, RelationModel, SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required
def create_content(request, slug,content_id=None):
    current_space = get_object_or_404(SpaceModel, slug=slug)
    all_topics = ContentModel.objects.filter(space=current_space.id).exclude(pk = content_id)
    current_relations= RelationModel.objects.filter(target_content=content_id)
    relationsform =[]
    for existing_content in all_topics.iterator():
        if(current_relations.filter(source_content = existing_content)):
            relationsform.append(
            {
                'id':existing_content.id,
                'value':1,
                'name': existing_content.title
            })
        else:
            relationsform.append(
            {
                'id':existing_content.id,
                'value':0,
                'name': existing_content.title
            })
    if content_id:
        content = get_object_or_404(ContentModel, pk=content_id)
    else:
        content = ContentModel(space_id = current_space.id, creator=request.user)
    form = CreateContentForm(request.POST or None, instance=content)
    if request.method == "POST":
        if form.is_valid():
            relations = request.POST.getlist('relation')
            new_content=form.save()
            RelationModel.objects.filter(target_content=content_id).delete()
            for rel in relations:
                pre_content = ContentModel.objects.get(pk=rel)
                RelationModel.objects.create(target_content=new_content,source_content=pre_content, creator=request.user,space=current_space)
            #return HttpResponseRedirect(reverse('swecourseapp:topics', args=(space_id,)))
            return redirect('spacedetails', slug=slug)    
    return render(request, 'pages/create-content.html', {'form': form, 'relationsform':relationsform})
