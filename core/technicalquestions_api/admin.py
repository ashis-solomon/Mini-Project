from django.contrib import admin
from technicalquestions_api.models import QuizQuestion
from .models import ResultTest

#admin.site.register(Results)
admin.site.register(QuizQuestion)

#admin.site.register(ResultUserResponse)
#admin.site.register(ResultScore)
#admin.site.register(ResultVisualization)
admin.site.register(ResultTest)