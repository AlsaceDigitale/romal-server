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

    def solve_proba(self):
        if self.times_tried:
            return min(self.times_solved/self.times_tried,1.0)
        else:
            return 1.0


class RunningChallenges(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.DO_NOTHING, related_name='running')
    current = models.BooleanField(default=False)
    #site = models.ForeignKey(Site, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.challenge)

    def get_solve_duration_min(self):
        return (self.end_time - self.start_time).total_seconds() / 60


class Trial(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.DO_NOTHING, related_name='trials')
    running_challenge = models.ForeignKey(RunningChallenges, on_delete=models.DO_NOTHING, related_name='trials')
    classes = models.CharField(max_length=5000)
    success = models.BooleanField()
    trial_time = models.DateTimeField(auto_now_add=True)
    player_pseudo = models.CharField(max_length=255, null=True, blank=True)
    player_email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "Trial for {}".format(self.challenge)


class Score(models.Model):
    player_pseudo = models.CharField(max_length=255)
    player_email = models.CharField(max_length=255, blank=True, null=True)
    score = models.PositiveIntegerField()
