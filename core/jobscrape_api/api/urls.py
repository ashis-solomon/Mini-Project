from django.urls import path
from jobscrape_api.api import views

urlpatterns = [
    # format -> /api/jobs/skills/?q=
    path('languages/', views.JobLanguageList.as_view(), name='job_language_list'),
    path('frameworks/', views.JobFrameworkList.as_view(), name='job_framework_list'),
    path('databases/', views.JobDatabaseList.as_view(), name='job_database_list'),
    path('skills/', views.JobSkillList.as_view(), name='job_skill_list'),
]
