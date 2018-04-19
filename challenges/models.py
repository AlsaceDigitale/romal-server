from django.db import models
from clarifai.rest import ClarifaiApp

class Challenge(models.Model):
    riddle_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=500)
    clarifai_model = models.CharField(default='general-v1.3', max_length=100)

    def solve(self, attemp_url):
        app = ClarifaiApp()
        model = app.models.get(self.clarifai_model)

        result = model.predict_by_url(attemp_url, lang='en')

        output = result['outputs'][0]

        for prediction in output['data']['concepts']:
            if prediction['name'] == self.answer_text:
                return { 'valid': True }

        return { 'valid': False, 'guessed': output['data'] }
