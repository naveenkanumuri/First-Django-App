from django.http import HttpResponse
import json

def route(request):

    message = {
        "message" : "Hello World!"
    }
    
    return HttpResponse(json.dumps(message))

# Create your views here.
