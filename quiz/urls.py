from django.urls import path
from .views import (
    create_quiz,
    create_question,
    all_quizes,
    attempt_quiz,
    created_quizes,
    attempted_quizes,
    update_question
)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("create-quiz/", create_quiz, name="create_quiz"),
    path("create-question/<int:space_id>/", create_question, name="create_question"),
    path("update-question/<int:space_id>/<int:quiz_id>/", update_question, name="update_question"),
    path("all-quizes/", all_quizes, name="all_quizes"),
    path("created-quizes/", created_quizes, name="created_quizes"),
    path("attempted-quizes/", attempted_quizes, name="attempted_quizes"),
    path("attempt-quiz/<int:id>/", attempt_quiz, name="attempt_quiz"),
]
