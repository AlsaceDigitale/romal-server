from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


def recognize(request):
    model_name = request.GET.get('model', 'general-v1.3')
    image_url = request.GET.get('image', '')
    if image_url == '':
        return HttpResponseBadRequest('image is mendatory')

    app = ClarifaiApp()
    model = app.models.get(model_name)
    image = ClImage(url=image_url)

    result = model.predict([image])

    if result['status']['code'] != 10000:
        return HttpResponseInternalServerError(result['status']['description'])

    output = result['outputs'][0]

    return JsonResponse({
        'status': 'ok',
        'model': output['model']['name'],
        'concepts': output['data']['concepts']
    })

