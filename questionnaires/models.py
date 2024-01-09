# SPDX-License-Identifier: Apache-2.0 #

from django.db import models
from accounts.models import User
from django.db.models import Sum, Max
from ckeditor.fields import RichTextField


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Questionnaire(DateMixin):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name

    def get_question_count(self):
        return Question.objects.filter(
            questionnaire=self, show_if_answer__isnull=True
        ).count()

    def get_section_total_score(self, section):
        return Question.objects.filter(questionnaire=self, section=section).aggregate(
            Sum("max_score")
        )["max_score__sum"]

    @property
    def total_score(self):
        return Question.objects.filter(questionnaire=self).aggregate(Sum("max_score"))[
            "max_score__sum"
        ]


class UserQuestionnaire(DateMixin):
    name = models.CharField(blank=False, max_length=100)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(
        Questionnaire, null=False, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    @property
    def progress(self):
        total = self.questionnaire.get_question_count()
        if total == 0:
            return 0
        return (
            Answer.objects.filter(
                user_questionnaire=self, option__question__show_if_answer__isnull=True
            )
            .distinct("option__question")
            .count()
            / total
        ) * 100

    @property
    def score(self):
        answers = Answer.objects.filter(user_questionnaire=self)
        if answers.count() == 0:
            return 0
        return (
            answers.aggregate(Sum("option__score"))["option__score__sum"]
            / self.questionnaire.total_score
        ) * 100

    @property
    def question_count(self):
        return self.questionnaire.get_question_count()

    def get_section_score(self, section):
        score = Answer.objects.filter(
            user_questionnaire=self, option__question__section=section
        ).aggregate(Sum("option__score"))["option__score__sum"]
        if not score:
            return 0
        return (score / self.questionnaire.get_section_total_score(section)) * 100


class Section(models.Model):
    slug = models.CharField(blank=False, max_length=20)
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(blank=False, max_length=30)
    description = models.TextField(blank=False, max_length=500)

    def __str__(self):
        return self.name


class Question(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaire, null=False, on_delete=models.PROTECT
    )
    section = models.ForeignKey(Section, null=False, on_delete=models.PROTECT)
    text = models.TextField(blank=False, max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    help_text = RichTextField(blank=True, max_length=2000, config_name="basic")
    min_answers = models.PositiveSmallIntegerField(default=1)
    max_answers = models.PositiveSmallIntegerField(default=1)
    max_score = models.PositiveSmallIntegerField(default=0)
    show_if_answer = models.ForeignKey(
        "questionnaires.QuestionOption",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="conditional_questions",
    )

    def __str__(self):
        return "{} - {}".format(self.order, self.text[0:20])

    def update_max_score(self):
        score = (
            QuestionOption.objects.filter(question=self)
            .order_by("-score")[: self.max_answers]
            .aggregate(Sum("score"))["score__sum"]
        ) or 0

        self.max_score = score

    def save(self, *args, **kwargs):
        self.update_max_score()
        super(Question, self).save(*args, **kwargs)


class QuestionOption(models.Model):
    question = models.ForeignKey(
        Question, null=False, on_delete=models.CASCADE, related_name="question_options"
    )
    text = models.CharField(blank=False, max_length=50)
    order = models.PositiveSmallIntegerField(default=1)
    score = models.PositiveSmallIntegerField(default=0)
    free_text_placeholder = models.CharField(blank=True, max_length=500)
    info_text = RichTextField(blank=True, max_length=300, config_name="minimal")
    next = models.ForeignKey(
        Question,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="question_options_conditional",
    )

    def __str__(self):
        return "Q {} - Opt {} - {}".format(
            self.question.order, self.order, self.text[0:10]
        )

    def save(self, *args, **kwargs):
        super(QuestionOption, self).save(*args, **kwargs)
        self.question.update_max_score()
        self.question.save()


class Answer(DateMixin):
    user_questionnaire = models.ForeignKey(
        UserQuestionnaire, null=False, on_delete=models.CASCADE
    )
    option = models.ForeignKey(QuestionOption, null=False, on_delete=models.PROTECT)
    text = models.TextField(blank=True, max_length=2000)


class ResultSuggestion(models.Model):
    min_score = models.PositiveSmallIntegerField(default=0)
    max_score = models.PositiveSmallIntegerField(default=100)
    section = models.ForeignKey(Section, null=False, on_delete=models.PROTECT)
    text = models.TextField(blank=False, max_length=3000)
