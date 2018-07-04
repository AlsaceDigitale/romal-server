import random

from django.db import transaction
from django.db.models import F, Manager
from django.db.models.functions import Greatest, Coalesce
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, FormParser
from django.contrib.sites.models import Site

from challenges.models import Challenge, RunningChallenges, Trial, Score
from challenges.serializers import ChallengeSerializer, RunningChallengeSerializer, ScoreSerializer
from challenges import services


def get_next_challenge(current_challenge: Challenge, current_running_challenge: RunningChallenges):
    all_challenges = Challenge.objects.all()

    current_challenge_proba = current_challenge.solve_proba()

    print("Current challenge proba: {}".format(current_challenge_proba))

    if current_running_challenge.get_solve_duration_min() > 5:
        print("Players are too dumb")
        next_challenges = filter(lambda c: c.solve_proba() >= current_challenge_proba, all_challenges)
    else:
        print("Players are too smart")
        next_challenges = filter(lambda c: c.solve_proba() <= current_challenge_proba, all_challenges)

    next_challenges = [n for n in next_challenges if n.id != current_challenge.id]

    if not next_challenges:
        next_challenges=list(Challenge.objects.all())

        next_challenges = [n for n in next_challenges if n.id != current_challenge.id]

    next_challenge = random.choice(next_challenges)

    print("Next challenge is {}".format(next_challenge))

    return next_challenge


class RunningChallengeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RunningChallenges.objects.filter(current=True)
    serializer_class = RunningChallengeSerializer


class ScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Score.objects
    serializer_class = ScoreSerializer


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
        current_running_challenge = RunningChallenges.objects. \
            filter(challenge=challenge,
                   current=True) \
            .first()  # type: RunningChallenges

        Challenge.objects.filter(id=challenge.id).update(times_tried=F('times_tried') + 1, last_tried=timezone.now())

        if request.query_params.get('fake_result', None):
            fake_result = request.query_params.get('fake_result')
            fake_result_bool = fake_result == 'true'
            solved, data = fake_result_bool, "{}"
        else:

            solved, data = services.solve_challenge(challenge, file_obj, filename)

        if solved:
            Challenge.objects.filter(id=challenge.id).update(times_solved=F('times_solved') + 1,
                                                             last_solved=timezone.now())

        else:
            Challenge.objects.filter(id=challenge.id).update(times_failed=F('times_failed') + 1,
                                                             last_failed=timezone.now())

        player_pseudo = request.query_params.get('player_pseudo', None)

        trial = Trial()
        trial.challenge = challenge
        trial.running_challenge = current_running_challenge
        trial.success = solved
        trial.classes = str(data)
        trial.player_pseudo = player_pseudo
        trial.save()

        if solved:
            with transaction.atomic():
                current_running_challenge = RunningChallenges.objects.select_for_update(). \
                    filter(challenge=challenge,
                           current=True) \
                    .first()  # type: RunningChallenges

                current_running_challenge.current = False
                current_running_challenge.end_time = timezone.now()
                new_running_challenge = RunningChallenges()
                new_running_challenge.challenge = get_next_challenge(challenge, current_running_challenge)
                new_running_challenge.current = True
                new_running_challenge.save()
                current_running_challenge.save()

                if player_pseudo:
                    score = Score.objects.filter(player_pseudo=player_pseudo).first()
                    if not score:
                        score = Score()
                        score.player_pseudo = player_pseudo
                        score.score = 0

                    score.score += 100

                    score.save()



        return Response(data={"solved": solved, "guessed": data})
