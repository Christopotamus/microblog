from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from wuphf.models import *

def get_main_wuphfs(request):
    if request.is_ajax() and "user" in request.session:
        #get wuphfs from database and return them as JSON
        try: 
            wuphfs = Wuphf.objects.get(author=request.session["userid"])
        except Wuphf.DoesNotExist:
            return HttpResponse("Dang! no wuphfs!")     
        else:
            return HttpResponse(simplejson.dumps(wuphfs))
    else:
        return HttpResponse(status=400)     


def post_new_wuphf(request):
    if request.is_ajax() and "user" in request.session and "userid" in request.session: 
        #print request.session["userid"] + ' ' + request.POST["content"]
        if "content" in request.POST:
            try:
                wuphf = Wuphf(author_id=int(request.session["userid"]), text=str(request.POST["content"]))
                wuphf.save()
                return HttpResponse("Wuphf sent!")
            except:
                return HttpResponse("damn it!")

