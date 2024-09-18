from django.shortcuts import redirect, render, get_object_or_404
from space.forms import UpdateSpaceModelForm
from space.models import SpaceModel
from django.contrib.auth.decorators  import login_required
import pywikibot

@login_required(login_url='/')
def update_space(request, slug):
    space=get_object_or_404(SpaceModel, slug=slug, author=request.user)
    form=UpdateSpaceModelForm(request.POST or None, files=request.FILES or None, instance=space)

    if form.is_valid():
        searchKeys= ''
        wikiItems = []
        if request.POST['wiki1'] and request.POST['tag1'] :
            space.tag1 =request.POST['tag1'] 
            space.wiki1 = request.POST['wiki1'] 
            wikiItems.append(request.POST['wiki1'])
        if request.POST['wiki2']and request.POST['tag2'] :
            space.tag2 =request.POST['tag2'] 
            space.wiki2 = request.POST['wiki2'] 
            wikiItems.append(request.POST['wiki2'])
        if request.POST['wiki3']and request.POST['tag3'] :
            space.tag3 =request.POST['tag3'] 
            space.wiki3 = request.POST['wiki3'] 
            wikiItems.append(request.POST['wiki3'])

        site = pywikibot.Site("wikidata","wikidata")
        repo = site.data_repository()
        for wikiItem in wikiItems:     
            item = pywikibot.ItemPage(repo,wikiItem)
            item_dict = item.get()
            clm_dict = item_dict["claims"]
            clm_list = clm_dict["P31"]
            for clm in clm_list:
                clm_trgt = clm.getTarget()
                clm_inst = clm_trgt.get()
                searchKeys = searchKeys + " " + clm_inst["labels"]["en"]
        space.searchwords = searchKeys
        form.save()
        return redirect('spacedetails', slug=space.slug)    

    return render(request,'pages/update-space.html', context={'form':form,'space':space})