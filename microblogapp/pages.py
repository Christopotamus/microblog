from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from wuphf.models import *

def get_main_wuphfs(request):
    if request.is_ajax() and "userid" in request.session and "username" in request.session:
        #get wuphfs from database and return them as JSON
        try: 
            #wuphfs = Wuphf(author_id=request.session["userid"])
            #get the subscribed ids
            user = Author.objects.get(username=request.session["username"])
            subbed = user.subscribed_ids.split(',')
            wuphf_list = Wuphf.objects.all().filter(author_id__in=subbed)
        except Wuphf.DoesNotExist:
            return HttpResponse("Dang! no wuphfs!")     
        else:
            data = serializers.serialize('json', wuphf_list)
            return HttpResponse(data)
    else:
        return HttpResponse(status=400)     


def post_new_wuphf(request):
    if request.is_ajax() and "username" in request.session and "userid" in request.session: 
        #print request.session["userid"] + ' ' + request.POST["content"]
        if "content" in request.POST:
            try:
                #username = request.session['username']
                #author = Author.objects.get(username=username)
                wuphf = Wuphf(author_id=int(request.session["userid"]),text=str(request.POST["content"]))
                #apparently python's special meaning for _ breaks the constuctor.
                wuphf.save()
                return HttpResponse("Wuphf sent!")
            except:
                return HttpResponse("damn it!")
    else:
        return HttpResponse(status=400)     
