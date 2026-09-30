
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.views.decorators.http import require_POST

from .models import Question, Answer, Upvote


# HOME PAGE
def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    questions = Question.objects.filter(is_approved=True)

    category = request.GET.get("category", "")
    search = request.GET.get("q", "").strip()

    if category and category in dict(Question.CATEGORIES):
        questions = questions.filter(category=category)

    if search:
        questions = questions.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
        )

    return render(request, "forum/home.html", {
        "questions": questions,
        "categories": Question.CATEGORIES,
        "selected_category": category,
        "search": search,
    })


# REGISTER
def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        "form": form
    })


# LOGIN
def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful!")
            return redirect("home")
    else:
        form = AuthenticationForm(request)

    return render(request, "registration/login.html", {
        "form": form
    })


# LOGOUT
@require_POST
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect("login")


# ASK A QUESTION
@login_required
def ask_question(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        category = request.POST.get("category", "Other")

        valid_categories = dict(Question.CATEGORIES)

        if (
            title
            and description
            and len(title) <= 200
            and category in valid_categories
        ):
            Question.objects.create(
                title=title,
                description=description,
                category=category
            )

            messages.success(request, "Your doubt has been posted!")
            return redirect("home")

        messages.error(
            request,
            "Please enter a valid title, description, and category."
        )

    return render(request, "forum/ask.html", {
        "categories": Question.CATEGORIES
    })


# QUESTION DETAILS AND ANSWERS
def question_detail(request, question_id):
    question = get_object_or_404(
        Question,
        id=question_id,
        is_approved=True
    )

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        body = request.POST.get("body", "").strip()

        if body and len(body) <= 5000:
            Answer.objects.create(
                question=question,
                body=body
            )

            messages.success(request, "Your answer has been posted!")

            return redirect(
                "question_detail",
                question_id=question.id
            )

        messages.error(request, "Please enter a valid answer.")

    answers = question.answers.filter(is_approved=True)

    return render(request, "forum/detail.html", {
        "question": question,
        "answers": answers
    })


# UPVOTE - ONE VOTE PER USER PER QUESTION
@require_POST
@login_required
def upvote_question(request, question_id):
    question = get_object_or_404(
        Question,
        id=question_id,
        is_approved=True
    )

    upvote, created = Upvote.objects.get_or_create(
        user=request.user,
        question=question
    )

    if created:
        Question.objects.filter(id=question.id).update(
            votes=F("votes") + 1
        )
        messages.success(request, "Your upvote has been recorded!")
    else:
        messages.info(
            request,
            "You have already upvoted this question."
        )

    return redirect(
        "question_detail",
        question_id=question.id
    )