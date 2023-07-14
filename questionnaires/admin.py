from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


class TabularQuestionOptionAdmin(admin.TabularInline):
    model = QuestionOption
    fk_name = "question"
    extra = 0
    fields = (
        "order",
        "score",
        "next",
        "text_en",
        "text_es",
        "info_text_en",
        "info_text_es",
        "free_text_placeholder_en",
        "free_text_placeholder_es",
    )
    readonly_fields = [
        "id",
    ]
    ordering = ("id",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "text",
    )
    fields = (
        "order",
        "questionnaire",
        "section",
        "min_answers",
        "max_answers",
        "max_score",
        "show_if_answer",
        "text_en",
        "text_es",
        "help_text_en",
        "help_text_es",
    )
    readonly_fields = ["id", "max_score"]
    ordering = ("id",)
    inlines = [TabularQuestionOptionAdmin]


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = [
        "id",
    ]
    ordering = ("id",)


@admin.register(UserQuestionnaire)
class UserQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = [
        "id",
    ]
    ordering = ("id",)


class TabularResultSuggestionAdmin(admin.TabularInline):
    model = ResultSuggestion
    extra = 0
    fields = ("min_score", "max_score", "text_en", "text_es")
    readonly_fields = [
        "id",
    ]
    ordering = ("id",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = (
        "order",
        "name_en",
        "name_es",
        "description_en",
        "description_es",
        "slug",
    )
    readonly_fields = [
        "id",
    ]
    ordering = ("id",)
    inlines = [TabularResultSuggestionAdmin]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "user_questionnaire", "text")
    readonly_fields = [
        "id",
    ]
    ordering = ("id",)
