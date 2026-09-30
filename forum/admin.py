
from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "votes",
        "created_at",
        "is_approved",
    )

    list_filter = (
        "category",
        "is_approved",
        "created_at",
    )

    search_fields = ("title", "description")
    list_editable = ("is_approved",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "created_at",
        "is_approved",
    )

    list_filter = ("is_approved", "created_at")
    search_fields = ("body", "question__title")
    list_editable = ("is_approved",)