
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("ask/", views.ask_question, name="ask_question"),
    path(
        "question/<int:question_id>/",
        views.question_detail,
        name="question_detail"
    ),
    path(
        "question/<int:question_id>/upvote/",
        views.upvote_question,
        name="upvote_question"
    ),
]