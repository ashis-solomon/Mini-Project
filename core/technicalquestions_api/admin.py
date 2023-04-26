from django.contrib import admin
from technicalquestions_api.models import QuizQuestion
from .models import ResultTest

admin.site.register(QuizQuestion)
admin.site.register(ResultTest)