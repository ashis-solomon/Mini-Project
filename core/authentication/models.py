from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, primary_key=True)
    rollno = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_groups',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_permissions',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

    def __str__(self):
        return self.username
