from django.db import models
from authentication.models import User


class Results(models.Model):
    testname = models.CharField(max_length=30)
    oops = models.IntegerField()
    dbms = models.IntegerField()
    cn = models.IntegerField()
    os = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Results")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.testname