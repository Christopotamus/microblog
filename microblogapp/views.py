from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from wuphf.models import *
import hashlib

def home(request):
    args = {}
    if "login_failed" in request.session:
        print request.session['login_failed']
        args = {"login_failed":request.session['login_failed']}
    if "user" in request.session:
        return render_to_response('index.html', {"user":request.session['user']},context_instance=RequestContext(request))
    else:
        return render_to_response('login.html', args,context_instance=RequestContext(request))

def login(request):
    if 'username' in request.POST and 'password' in request.POST:
        if request.POST['username'] != '' and request.POST['password'] != '':
            username = request.POST['username']
            password = hashlib.md5(request.POST['password']).hexdigest()
            try:
                user = auth_users.objects.get(username=username, password=password)
            except auth_users.DoesNotExist:
                request.session['login_failed'] = True
                return redirect('/')
            else:
                request.session['user'] = user.username
                request.session['login_failed'] = False 
                return redirect('/')

    request.session['login_failed'] = True
    return redirect('/')

def logout(request):
    if "user" in request.session:
        del request.session['user']

    return redirect('/')
