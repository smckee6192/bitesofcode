import datetime
# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('template.html', context_dict, context)