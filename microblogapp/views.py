from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse

def home(request):
    if "user" in request.session:
        print request.session['user']
    else:
        request.session['user'] = 'Chris'

    return render_to_response('index.html', '',context_instance=RequestContext(request))
