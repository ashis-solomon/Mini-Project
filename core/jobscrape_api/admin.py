from django.contrib import admin
from jobscrape_api.models import JobLanguages, JobFrameworks, JobDatabases, JobSkills

admin.site.register(JobLanguages)
admin.site.register(JobFrameworks)
admin.site.register(JobDatabases)
admin.site.register(JobSkills)