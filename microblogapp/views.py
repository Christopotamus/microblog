from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from wuphf.models import *
import hashlib

def isLoggedIn(request):
    if "user" in request.session:
        return True
    else:
        return False

def home(request):
    args = {}
    if isLoggedIn(request) and "user" in request.session:
        args = {"logged_in":True, "user":request.session['user']}
    
    
    return render_to_response('index.html', args,context_instance=RequestContext(request))

def register(request):
    args = {}

    if "username" in request.POST and "password" in request.POST and "fullname" in request.POST:
        hashedPW = hashlib.md5(request.POST['password']).hexdigest()
        new_user = Author(username=request.POST['username'],password=hashedPW,fullname=request.POST['fullname'])
    try: 
        user = Author.objects.get(username=new_user.username)
    except Author.DoesNotExist:
        new_user.save()
        args = {'success':True}
    else:
        args = {'success':False}

    #validate fields
    #send confirmation email
    #check for matches on username OR email 
    return render_to_response('/register/',args,context_instance=RequestContext(request))

def login(request):
    if "user" in request.session:
        del request.session['user']

    if 'username' in request.POST and 'password' in request.POST:
        if request.POST['username'] != '' and request.POST['password'] != '':
            username = request.POST['username']
            password = hashlib.md5(request.POST['password']).hexdigest()
            try:
                user = auth_users.objects.get(username=username, password=password)
            except auth_users.DoesNotExist:
                return redirect('/')
            else:
                request.session['user'] = user.username
                return redirect('/home')

    return redirect('/')

def logout(request):
    if "user" in request.session:
        del request.session['user']

    return redirect('/')
