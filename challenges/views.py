from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotFound
from django.forms.models import model_to_dict

from .models import Challenge

# Will disappear when we have a way to set the current challenge
def index(request):
    challenges = Challenge.objects.all()

    return JsonResponse({
        "challenges": list(challenges.values('riddle_text', 'id')),
    })

def details(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)

    return JsonResponse({
        "challenge": {
            "riddle_text": challenge.riddle_text,
            "id": challenge.id,
        },
    })

def solve(request, challenge_id):
    if request.method != 'POST':
        return HttpResponseNotFound('Not found')

    attemp_url = request.POST.get('attempt', '')
    if attemp_url == '':
        return HttpResponseBadRequest('attempt is mendatory')

    challenge = get_object_or_404(Challenge, pk=challenge_id)

    response = challenge.solve(attemp_url)

    if response['valid']:
        return JsonResponse({
            "solved": True,
            "text": "GGWP",
        })

    return JsonResponse({
        "solved": False,
        "text": "Nice try!",
        "guessed": response['guessed'],
    })
