from rest_framework import generics
from rest_framework.response import Response
from jobscrape_api.models import JobLanguage, JobFramework, JobDatabase, JobSkill
from jobscrape_api.api.serializers import JobLanguageSerializer, JobFrameworkSerializer, JobDatabaseSerializer, JobSkillSerializer


class JobLanguageList(generics.ListAPIView):
    serializer_class = JobLanguageSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return JobLanguage.objects.filter(language__icontains=query)
        return JobLanguage.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [language['language'] for language in serializer.data]
        return Response(data)


class JobFrameworkList(generics.ListAPIView):
    serializer_class = JobFrameworkSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return JobFramework.objects.filter(framework__icontains=query)
        return JobFramework.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [framework['framework'] for framework in serializer.data]
        return Response(data)


class JobDatabaseList(generics.ListAPIView):
    serializer_class = JobDatabaseSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return JobDatabase.objects.filter(database__icontains=query)
        return JobDatabase.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [database['database'] for database in serializer.data]
        return Response(data)

class JobSkillList(generics.ListAPIView):
    serializer_class = JobSkillSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return JobSkill.objects.filter(skill__icontains=query)
        return JobSkill.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [skill['skill'] for skill in serializer.data]
        return Response(data)
