from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import io
import base64

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
