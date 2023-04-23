from django.urls import path, include
from rest_framework import routers
from technicalquestions_api.api.views import ResultsViewSet

router = routers.DefaultRouter()
router.register(r'results', ResultsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]