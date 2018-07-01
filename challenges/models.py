import datetime

from django.db import models
from django.contrib.sites.models import Site

class Challenge(models.Model):
    riddle_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=500)
    classes_list = models.CharField(max_length=150)
    clarifai_model = models.CharField(default='general-v1.3', max_length=100)
    times_tried = models.PositiveIntegerField(default=0)
    last_tried = models.DateTimeField(default=datetime.datetime(1970,1,1))
    times_solved = models.PositiveIntegerField(default=0)
    last_solved = models.DateTimeField(default=datetime.datetime(1970, 1, 1))
    times_failed = models.PositiveIntegerField(default=0)
    last_failed = models.DateTimeField(default=datetime.datetime(1970, 1, 1))

    def __str__(self):
        return self.riddle_text


class RunningChallenges(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.DO_NOTHING, related_name='running')
    #site = models.ForeignKey(Site, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.challenge)

