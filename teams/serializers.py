from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'id', 'score']
        read_only_fields = ['score']