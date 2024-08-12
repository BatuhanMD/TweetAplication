from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=30)
    message = models.CharField(max_length=255)


    def __str__(self):
        return f"Nick: {self.nickname}, Tweet: {self.message}"