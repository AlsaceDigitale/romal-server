from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import io
import base64

def solve_challenge(challenge, file_obj, filename):
    app = ClarifaiApp()
    model = app.models.get(challenge.clarifai_model)

    image = ClImage(file_obj=io.BytesIO(base64.b64decode(file_obj.read())))
    result = model.predict([image])

    output = result['outputs'][0]

    for prediction in output['data']['concepts']:
        if prediction['name'] == challenge.answer_text:
            return True, None

    return False, output['data']['concepts']
