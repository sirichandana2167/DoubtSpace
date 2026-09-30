
from django.conf import settings
from django.db import models


class Question(models.Model):
    CATEGORIES = [
        ("DSA", "Data Structures & Algorithms"),
        ("Java", "Java"),
        ("Python", "Python"),
        ("DBMS", "Database Management"),
        ("Web Development", "Web Development"),
        ("Computer Networks", "Computer Networks"),
        ("Operating Systems", "Operating Systems"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        default="Other"
    )
    votes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Answer to {self.question.title}"


class Upvote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="upvotes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "question"],
                name="unique_user_question_upvote"
            )
        ]

    def __str__(self):
        return f"{self.user.username} upvoted {self.question.title}"