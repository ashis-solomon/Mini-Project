from django.contrib import admin
from jobscrape_api.models import JobLanguage, JobFramework, JobDatabase, JobSkill

admin.site.register(JobLanguage)
admin.site.register(JobFramework)
admin.site.register(JobDatabase)
admin.site.register(JobSkill)