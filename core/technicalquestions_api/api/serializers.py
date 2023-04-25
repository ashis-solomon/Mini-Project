from rest_framework import serializers

from technicalquestions_api.models import QuizQuestion
from technicalquestions_api.models import ResultTest

# class ResultsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Results
#         fields="__all__"

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuizQuestion
        fields="__all__"   


# class ResultUserResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResultUserResponse
#         fields = ['question_id', 'answer']


# class ResultScoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResultScore
#         fields = ['cn_score', 'dbms_score', 'oops_score', 'os_score', 'total_score']


# class ResultVisualizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResultVisualization
#         fields = ['CO1_correct', 'CO2_correct', 'CO3_correct', 'CO4_correct',
#                   'CO1_total', 'CO2_total', 'CO3_total', 'CO4_total',
#                   'easy_correct', 'medium_correct', 'hard_correct',
#                   'easy_total', 'medium_total', 'hard_total',
#                   'sub1_correct', 'sub2_correct', 'sub3_correct', 'sub4_correct']


class ResultTestSerializer(serializers.ModelSerializer):
    # user_responses = ResultUserResponseSerializer(many=True)
    # scores = ResultScoreSerializer()
    # visualization = ResultVisualizationSerializer()

    class Meta:
        model = ResultTest
        fields="__all__" 


# class ResultTestCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResultTest
#         fields = ['user', 'user_responses', 'scores', 'visualization']