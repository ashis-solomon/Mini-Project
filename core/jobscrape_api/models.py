from django.db import models


class JobLanguage(models.Model):
    language = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.language}'

class JobFramework(models.Model):
    framework = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.framework}'

class JobDatabase(models.Model):
    database = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.database}'

class JobSkill(models.Model):
    skill = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.skill}'
