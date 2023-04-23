from rest_framework.response import Response
from rest_framework.views import APIView


class ApiOverviewAV(APIView):
    def get(self, request, format=None):
        overview = [
            " /api/auth/     - Authentication ",
            " /api/          - TechnicalQuestions API ",
            " /api/leetcode/ - Leetcode API ",
        ]
        return Response(overview)