from django.contrib import admin

from challenges.models import Challenge, RunningChallenges

admin.site.register(Challenge)
admin.site.register(RunningChallenges)
