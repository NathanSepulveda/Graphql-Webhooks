from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


class WebhookView(View):
    def get(self, request, **kwargs):
        return HttpResponse("Hi")
    def post(self, request, object_id=None, **kwargs):
        payload = json.loads(request.body)

        response = json.dumps(payload, indent=4)
#          return HttpResponse(response, content_type='application/json')
        print(response)
        return HttpResponse()