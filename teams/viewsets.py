from rest_framework import viewsets, status
from teams.serializers import TeamSerializer
from teams.models import Team
from rest_framework import mixins

class TeamViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
