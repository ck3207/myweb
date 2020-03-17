from django.db import models
from django.contrib import admin
# Create your models here.



class Mood(models.Model):
    """Load Data From Pickle File."""
    mood = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.mood


class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, default='nickname')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.message

