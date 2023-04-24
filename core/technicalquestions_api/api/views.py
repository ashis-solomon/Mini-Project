from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, status

from technicalquestions_api.models import Results,QuizQuestion
from technicalquestions_api.api.serializers import ResultsSerializer,QuizQuestionSerializer

from random import sample
from collections import defaultdict

from ..models import ResultTest
from .serializers import ResultTestSerializer, ResultTestCreateSerializer

class ResultsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = ResultsSerializer
    queryset = Results.objects.all()

class QuizQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = QuizQuestionSerializer
    queryset = QuizQuestion.objects.all() 

class GenerateTechnicalQuestionsView(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self, request):
        # Get all questions from the database grouped by subject
        questions_by_subject = defaultdict(list)
        for question in QuizQuestion.objects.all():
            questions_by_subject[question.subject].append(question)

        # Select 10 random questions for each subject
        questions = []
        for subject, subject_questions in questions_by_subject.items():
            questions += sample(subject_questions, 10)

        # Serialize the questions data to JSON
        data = [{
            'question_id': question.question_id,
            'topic': question.topic,
            'question': question.question,
            'option_a': question.option_a,
            'option_b': question.option_b,
            'option_c': question.option_c,
            'option_d': question.option_d,
            'correct_answer': question.correct_answer,
            'difficulty': question.difficulty,
            'cognitive_level': question.cognitive_level,
            'subject': question.subject,
        } for question in questions]

        # Return the questions data in a JSON response
        return Response(data)
    

class ResultTestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = ResultTestSerializer

    def get_queryset(self):
        # print(self.request.user)
        # return ResultTest.objects.filter(user=self.request.user)
        return ResultTest.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ResultTestCreateSerializer(data=request.data)
        if serializer.is_valid():
            test = serializer.save(user=request.user)
            serializer = ResultTestSerializer(test)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ResultTestUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResultTestSerializer

    def get_queryset(self):
        print(self.request.user)
        return ResultTest.objects.filter(user=self.request.user)
    

class ResultTestUserDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResultTestSerializer

    def get_object(self):
        queryset = ResultTest.objects.filter(user=self.request.user)
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj