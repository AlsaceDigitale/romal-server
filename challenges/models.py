from django.db import models
from django.contrib.sites.models import Site

class Challenge(models.Model):
    riddle_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=500)
    classes_list = models.CharField(max_length=150)
    clarifai_model = models.CharField(default='general-v1.3', max_length=100)

    def __str__(self):
        return self.riddle_text


class RunningChallenges(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.DO_NOTHING, related_name='running')
    #site = models.ForeignKey(Site, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.challenge)

