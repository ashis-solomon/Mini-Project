from rest_framework import serializers

from technicalquestions_api.models import Results,QuizQuestion
from technicalquestions_api.models import ResultUserResponse, ResultScore, ResultVisualization, ResultTest

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Results
        fields="__all__"

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuizQuestion
        fields="__all__"   


class ResultUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultUserResponse
        fields = ['question_id', 'answer']


class ResultScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultScore
        fields = ['cn_score', 'dbms_score', 'oops_score', 'os_score', 'total_score']


class ResultVisualizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultVisualization
        fields="__all__"


class ResultTestSerializer(serializers.ModelSerializer):
    user_responses = ResultUserResponseSerializer(many=True)
    scores = ResultScoreSerializer()
    visualization = ResultVisualizationSerializer()

    class Meta:
        model = ResultTest
        fields = ['id', 'user', 'test_date', 'user_responses', 'scores', 'visualization']


class ResultTestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultTest
        fields = ['user', 'user_responses', 'scores', 'visualization']