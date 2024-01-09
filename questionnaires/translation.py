# SPDX-License-Identifier: Apache-2.0 #

from modeltranslation.translator import register, TranslationOptions
from .models import Question, QuestionOption, Section, ResultSuggestion


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = (
        "text",
        "help_text",
    )


@register(QuestionOption)
class QuestionOptionTranslationOptions(TranslationOptions):
    fields = ("text", "info_text", "free_text_placeholder")


@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


@register(ResultSuggestion)
class ResultSuggestionTranslationOptions(TranslationOptions):
    fields = ("text",)
