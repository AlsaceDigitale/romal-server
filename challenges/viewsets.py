from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from django.contrib.sites.models import Site

from challenges.models import Challenge
from challenges.serializers import ChallengeSerializer
from challenges import services

class ChallengeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.filter(running__site=Site.objects.get_current())
    serializer_class = ChallengeSerializer


    @action(methods=['post'], detail=True, parser_classes=(FileUploadParser,))
    def solve(self, request, pk=None, format=None, filename=None):
        challenge = self.get_object()
        file_obj = request.data['file']
        if file_obj is None:
            return Response(data="attempt is mendatory", status=status.HTTP_400_BAD_REQUEST)

        solved, data = services.solve_challenge(challenge, file_obj.chunks(), filename)

        return Response(data={"solved": solved, "guessed": data})
