from .models import *
from rest_framework import serializers


class UserQuestionnaireSerializer(serializers.ModelSerializer):
    questionCount = serializers.SerializerMethodField()

    class Meta:
        model = UserQuestionnaire
        fields = ("name", "id", "questionCount", "score", "progress")

    def get_questionCount(self, instance):
        return instance.question_count


class SectionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = (
            "name",
            "description",
            "questions",
            "slug",
            "id",
        )

    def get_questions(self, instance):
        return []


class MinimalQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ("id",)


class MinimalQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id",)


class QuestionOptionSerializer(serializers.ModelSerializer):
    freeText = serializers.SerializerMethodField()
    freeTextPlaceholder = serializers.SerializerMethodField()
    helpText = serializers.SerializerMethodField()

    class Meta:
        model = QuestionOption
        fields = (
            "id",
            "text",
            "next",
            "freeText",
            "freeTextPlaceholder",
            "helpText",
        )

    def get_freeText(self, instance):
        return len(instance.free_text_placeholder) > 0

    def get_freeTextPlaceholder(self, instance):
        return instance.free_text_placeholder

    def get_helpText(self, instance):
        return instance.info_text


class QuestionSerializer(serializers.ModelSerializer):
    sectionId = serializers.SerializerMethodField()
    optionParent = serializers.SerializerMethodField()
    helpText = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    minSelect = serializers.SerializerMethodField()
    maxSelect = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            "id",
            "text",
            "sectionId",
            "options",
            "optionParent",
            "helpText",
            "minSelect",
            "maxSelect",
        )

    def get_sectionId(self, instance):
        return instance.section.id

    def get_optionParent(self, instance):
        if instance.show_if_answer:
            return instance.show_if_answer.id
        return None

    def get_helpText(self, instance):
        return instance.help_text

    def get_options(self, instance):
        return QuestionOptionSerializer(
            instance.question_options.order_by("order"), many=True
        ).data

    def get_minSelect(self, instance):
        return instance.min_answers

    def get_maxSelect(self, instance):
        return instance.max_answers


class AnswerSerializer(serializers.ModelSerializer):
    option = MinimalQuestionOptionSerializer()
    question = serializers.SerializerMethodField()

    class Meta:
        model = QuestionOption
        fields = (
            "text",
            "question",
            "option",
        )

    def get_question(self, instance):
        return MinimalQuestionSerializer(instance.option.question).data
