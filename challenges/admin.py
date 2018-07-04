from django.contrib import admin
from django.contrib.admin import ModelAdmin

from challenges.models import Challenge, RunningChallenges, Trial, GameStatus


@admin.register(Challenge)
class ChallengeAdmin(ModelAdmin):
    list_display = ['riddle_text', 'answer_text']


@admin.register(RunningChallenges)
class RunningChallengesAdmin(ModelAdmin):

    list_display = ['challenge', 'start_time', 'end_time', 'current']


@admin.register(Trial)
class TrialAdmin(ModelAdmin):
    list_display = ['challenge', 'trial_time', 'classes', 'player_pseudo', 'success']


@admin.register(GameStatus)
class GameStatusAdmin(ModelAdmin):

    list_display = ['status_date', 'current', 'monster_score']