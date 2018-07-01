from django.db.models import F
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, FormParser
from django.contrib.sites.models import Site

from challenges.models import Challenge, RunningChallenges
from challenges.serializers import ChallengeSerializer
from challenges import services


def get_next_challenge():
    return Challenge.objects.filter().first()


class ChallengeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    parser_classes = (FormParser,)


    @action(methods=['post'], detail=True, parser_classes=(FileUploadParser,))
    def solve(self, request, pk=None, format=None, filename=None):
        file_obj = request.FILES['file']

        if file_obj is None:
            return Response(data="attempt is mandatory", status=status.HTTP_400_BAD_REQUEST)

        challenge = self.get_object()

        Challenge.objects.filter(id=challenge.id).update(times_tried=F('times_tried') + 1, last_tried=timezone.now())

        solved, data = services.solve_challenge(challenge, file_obj, filename)

        if solved:
            Challenge.objects.filter(id=challenge.id).update(times_solved=F('times_solved') + 1,
                                                             last_solved=timezone.now())

        else:
            Challenge.objects.filter(id=challenge.id).update(times_failed=F('times_failed') + 1,
                                                             last_failed=timezone.now())

        if solved:
            current_running_challenge=RunningChallenges.objects.filter(challenge=challenge).first()
            current_running_challenge.challenge = get_next_challenge()
            current_running_challenge.save()

        return Response(data={"solved": solved, "guessed": data})
