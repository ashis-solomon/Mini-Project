from django.urls import path, include
from rest_framework import routers
from technicalquestions_api.api.views import QuizQuestionViewSet, GenerateTechnicalQuestionsView
from .views import ResultTestListCreateView, ResultTestUserView, ResultTestUserDetailView


router = routers.DefaultRouter()
#router.register(r'results', ResultsViewSet)
router.register(r'questions', QuizQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('question/generate/', GenerateTechnicalQuestionsView.as_view(), name='generate-technical-questions'), 
    # route changed from questions to question to avoid url match error

    path('prev-results/', ResultTestListCreateView.as_view(), name='result_test_list_create'),
    # for admin 

    path('prev-results/user/', ResultTestUserView.as_view(), name='result_test_user_list'),
    # for logged in user to view past results

    path('prev-results/user/<int:pk>/', ResultTestUserDetailView.as_view(), name='result_test_user_detail'),
    # for logged in user to view a specific past result
]