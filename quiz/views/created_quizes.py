from django.shortcuts import redirect, render
from quiz.forms import CreateQuizModelForm, CreateQuestionModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz.models import QuizModel, QuestionModel
from django.contrib.auth.decorators  import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import JsonResponse


@login_required(login_url='/')
def created_quizes(request): 

    allquizes=QuizModel.objects.filter(creator=request.user)

    page=request.GET.get('page')
    paginator=Paginator(allquizes,3)

    return render(request,'quizes.html', context={'allquizes':paginator.get_page(page)})