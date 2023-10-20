from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    model = QuestionOption
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
    search_fields = (
        "question__order",
        "text",
    )
    ordering = ("id",)

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(question__order=search_term_as_int)
        return queryset, may_have_duplicates


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
    autocomplete_fields = [
        "next",
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "order",
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
    ordering = ("order",)
    inlines = [TabularQuestionOptionAdmin]
    search_fields = (
        "order",
        "text",
    )
    autocomplete_fields = [
        "show_if_answer",
    ]


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
