from django.db import models
from authentication.models import User


class Results(models.Model):
    testname = models.CharField(max_length=30)
    oops = models.IntegerField()
    dbms = models.IntegerField()
    cn = models.IntegerField()
    os = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.testname
    
class QuizQuestion(models.Model):
    question_id = models.IntegerField(primary_key=True, auto_created=True)
    topic = models.CharField(max_length=5000)
    question = models.TextField(max_length=5000)
    option_a = models.CharField(max_length=5000)
    option_b = models.CharField(max_length=5000)
    option_c = models.CharField(max_length=5000)
    option_d = models.CharField(max_length=5000)
    correct_answer = models.CharField(max_length=5000)
    difficulty = models.CharField(max_length=5000)
    cognitive_level = models.CharField(max_length=5000)
    subject = models.CharField(max_length=5000)    

    def __str__(self):
        return self.question 