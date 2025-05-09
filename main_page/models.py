from django.db import models


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    telegram = models.CharField(max_length=100)
    about = models.TextField()
