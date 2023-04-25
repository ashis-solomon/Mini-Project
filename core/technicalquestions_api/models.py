from email.policy import default
from django.db import models
from authentication.models import User


# class Results(models.Model):
#     testname = models.CharField(max_length=30)
#     oops = models.IntegerField()
#     dbms = models.IntegerField()
#     cn = models.IntegerField()
#     os = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.testname
    
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
    


# class ResultUserResponse(models.Model):
#     question_id = models.IntegerField()
#     answer = models.CharField(max_length=1)

#     def __str__(self):
#         return f'{self.question_id}  {self.answer}'


# class ResultScore(models.Model):
#     cn_score = models.FloatField()
#     dbms_score = models.FloatField()
#     oops_score = models.FloatField()
#     os_score = models.FloatField()
#     total_score = models.FloatField()

#     def __str__(self):
#         return f'{self.total_score}'


# class ResultVisualization(models.Model):
#     CO1_correct = models.IntegerField()
#     CO2_correct = models.IntegerField()
#     CO3_correct = models.IntegerField()
#     CO4_correct = models.IntegerField()

#     CO1_total = models.IntegerField()
#     CO2_total = models.IntegerField()
#     CO3_total = models.IntegerField()
#     CO4_total = models.IntegerField()

#     easy_correct = models.IntegerField()
#     medium_correct = models.IntegerField()
#     hard_correct = models.IntegerField()

#     easy_total = models.IntegerField()
#     medium_total = models.IntegerField()
#     hard_total = models.IntegerField()

#     sub1_correct = models.IntegerField()
#     sub2_correct = models.IntegerField()
#     sub3_correct = models.IntegerField()
#     sub4_correct = models.IntegerField()


class ResultTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="results")
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_date = models.DateTimeField(auto_now_add=True)
    results=models.JSONField()
    #user_responses = models.ManyToManyField(ResultUserResponse)
    #scores = models.ForeignKey(ResultScore, on_delete=models.CASCADE)
    #visualization = models.ForeignKey(ResultVisualization, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}  \
                {self.test_date}'