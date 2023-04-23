from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from technicalquestions_api.models import Results
from technicalquestions_api.api.serializers import ResultsSerializer

class ResultsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = ResultsSerializer
    queryset = Results.objects.all()