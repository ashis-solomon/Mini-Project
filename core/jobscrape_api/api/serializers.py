from rest_framework import serializers
from jobscrape_api.models import JobLanguage, JobFramework, JobDatabase, JobSkill

class JobLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLanguage
        fields = ['language']

class JobFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobFramework
        fields = ['framework']

class JobDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDatabase
        fields = ['database']

class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = ['skill']
