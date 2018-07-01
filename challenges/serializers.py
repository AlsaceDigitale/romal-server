from rest_framework import serializers
from challenges.models import Challenge, RunningChallenges, Score


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['riddle_text', 'id']


class RunningChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningChallenges
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"