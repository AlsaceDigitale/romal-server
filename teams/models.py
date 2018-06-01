from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=500)
    score = models.IntegerField(default=0)
