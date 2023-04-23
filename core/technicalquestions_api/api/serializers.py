from rest_framework import serializers

from technicalquestions_api.models import Results

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Results
        fields="__all__"