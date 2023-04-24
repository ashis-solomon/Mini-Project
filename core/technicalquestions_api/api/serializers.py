from rest_framework import serializers

from technicalquestions_api.models import Results,QuizQuestion

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Results
        fields="__all__"

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuizQuestion
        fields="__all__"   