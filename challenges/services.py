from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

def solve_challenge(challenge, file_obj, filename):
    app = ClarifaiApp()
    model = app.models.get(challenge.clarifai_model)

    image = ClImage(file_obj=file_obj, filename=filename)
    result = model.predict([image])

    output = result['outputs'][0]

    for prediction in output['data']['concepts']:
        if prediction['name'] == challenge.answer_text:
            return True, None

    return False, output['data']['concepts']
