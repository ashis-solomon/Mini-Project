from django.urls import path, include
from rest_framework import routers
from technicalquestions_api.api.views import ResultsViewSet, QuizQuestionViewSet, GenerateTechnicalQuestionsView

router = routers.DefaultRouter()
router.register(r'results', ResultsViewSet)
router.register(r'questions', QuizQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('question/generate/', GenerateTechnicalQuestionsView.as_view(), name='generate-technical-questions'), 
    # route changed from questions to question to avoid url match error
]