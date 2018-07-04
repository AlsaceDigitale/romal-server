from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import io
import base64

from django.db import transaction

from challenges.models import GameStatus
from challenges.tools import Timer


def solve_challenge(challenge, file_obj, filename):
    expected_classes = [s.strip() for s in challenge.classes_list.split(',')]

    with Timer() as t1:
        app = ClarifaiApp()

    print("Clarifai app init took {:.3f}s".format(t1.interval))

    model = app.models.get(challenge.clarifai_model)

    with Timer() as t2:
        image = ClImage(file_obj=io.BytesIO(base64.b64decode(file_obj.read())))

    print("Clarifai image loading took {:.3f}s".format(t2.interval))

    with Timer() as t3:
        result = model.predict([image])

    print("Clarifai image model prediction took {:.3f}s".format(t3.interval))

    output = result['outputs'][0]

    for prediction in output['data']['concepts']:
        if prediction['name'] in expected_classes:
            return True, None

    return False, output['data']['concepts']


def update_monster_score(score_delta: int):
    with transaction.atomic():
        if GameStatus.objects.count() == 0:
            current_game_status = GameStatus()
            current_game_status.monster_score = 0
            current_game_status.current = True
            current_game_status.save()
        else:
            current_game_status = GameStatus.objects.select_for_update().filter(current=True).first()

        new_game_status = GameStatus()
        new_game_status.monster_score = current_game_status.monster_score + score_delta

        if new_game_status.monster_score < 0:
            if current_game_status.monster_score > 0:
                new_game_status.monster_score = 0
            else:
                print("No updating score because would be under 0")
                return

        new_game_status.current = True
        current_game_status.current = False

        current_game_status.save()
        new_game_status.save()

        print("New monster score: {}".format(new_game_status.monster_score))
