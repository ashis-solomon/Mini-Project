from django.db import models


class JobLanguages(models.Model):
    language = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.language}'

class JobFrameworks(models.Model):
    framework = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.framework}'

class JobDatabases(models.Model):
    database = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.database}'

class JobSkills(models.Model):
    skill = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.skill}'
