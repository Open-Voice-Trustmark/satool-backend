from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
import json


class UserQuestionnaireViewSet(ModelViewSet):
    lookup_field = "id"
    permissions = [IsAuthenticated]
    serializer_class = UserQuestionnaireSerializer

    def get_queryset(self):
        return UserQuestionnaire.objects.filter(user=self.request.user.id).order_by(
            "-created_at"
        )


class CreateQuestionnaireView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = json.loads(request.body)
        questionnaire = Questionnaire.objects.all().first()
        user_questionnaire = UserQuestionnaire.objects.create(
            questionnaire=questionnaire,
            user=request.user,
            name=data["name"],
        )
        return Response({"id": user_questionnaire.id})


class QuestionViewSet(ModelViewSet):
    lookup_field = "id"
    permissions = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def list(self, request, questionnaire, section=None, question=None):
        user_questionnaire = UserQuestionnaire.objects.filter(
            id=questionnaire, user=request.user.id
        ).first()
        print(request.user.id)
        if not user_questionnaire:
            raise ParseError("No questions for this questionnaire")
        if question:
            section = Question.objects.get(id=question).section
        data = QuestionSerializer(
            Question.objects.filter(
                questionnaire=user_questionnaire.questionnaire, section=section
            ).order_by("order"),
            many=True,
        ).data
        return Response(data)


class SectionViewSet(ModelViewSet):
    lookup_field = "id"
    permissions = [IsAuthenticated]
    serializer_class = SectionSerializer
    queryset = Section.objects.all().order_by("order")


class ResultsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, questionnaire):
        user_questionnaire = UserQuestionnaire.objects.filter(
            id=questionnaire, user=request.user.id
        ).first()
        if not user_questionnaire:
            raise ParseError("No questions for this questionnaire")

        sections = Section.objects.all().order_by("order")
        section_results = []
        for section in sections:
            score = user_questionnaire.get_section_score(section)
            suggestions = ResultSuggestion.objects.filter(
                min_score__lte=score, max_score__gte=score, section=section
            ).order_by("min_score")
            texts = []
            for suggestion in suggestions:
                texts.append(suggestion.text)
            r = {
                "slug": section.slug,
                "name": section.name,
                "score": score,
                "suggestions": texts,
            }
            section_results.append(r)

        return Response(
            {"sections": section_results, "score": user_questionnaire.score}
        )


class QuestionnaireView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, questionnaire):
        user_questionnaire = UserQuestionnaire.objects.filter(
            id=questionnaire, user=request.user.id
        ).first()
        print(request.user.id)
        if not user_questionnaire:
            raise ParseError("No questions for this questionnaire")

        answers = Answer.objects.filter(user_questionnaire=user_questionnaire)

        return Response(
            {
                "questionnaire": UserQuestionnaireSerializer(user_questionnaire).data,
                "answers": AnswerSerializer(answers, many=True).data,
            }
        )


class AnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, questionnaire):
        user_questionnaire = UserQuestionnaire.objects.filter(
            id=questionnaire, user=request.user.id
        ).first()
        if not user_questionnaire:
            raise ParseError("No questions for this questionnaire")

        answers = request.data["answers"]

        db_answers = []
        Answer.objects.filter(user_questionnaire=user_questionnaire).delete()
        for answer in answers:
            text = ""
            if "text" in answer:
                text = answer["text"]
            db_answers.append(
                Answer(
                    user_questionnaire=user_questionnaire,
                    option_id=answer["option"]["id"],
                    text=text,
                )
            )
        Answer.objects.bulk_create(db_answers)

        return Response({})
