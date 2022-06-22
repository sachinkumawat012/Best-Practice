from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

# part1

# class Books(models.Model):
#     title = models.CharField(max_length=100)
#     excerpt = models.TextField()

#     def __str__(self) -> str:
#         return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Quizzes(models.Model):
    title = models.CharField(max_length=225, default=_('New Quiz'))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    SCAL = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )

    TYPE = (
        (0, _('Bultiple_Choice')),
    )

    title = models.CharField(max_length=225, verbose_name=_("Title"))
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of question"))
    difficulty = models.IntegerField(choices=SCAL, default=0, verbose_name=_("Difficulty"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=("Date Created"))

    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer_text