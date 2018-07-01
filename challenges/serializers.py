from rest_framework import serializers
from challenges.models import Challenge, RunningChallenges


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['riddle_text', 'id']


class RunningChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningChallenges
        fields = "__all__"
