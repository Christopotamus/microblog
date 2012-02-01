from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.core.mail import send_mail
from wuphf.models import *
import hashlib, random, re

def isLoggedIn(request):
    if "user" in request.session:
        return True
    else:
        return False

def home(request):
    args = {}
    if isLoggedIn(request):
        args = {"logged_in":True, "user":request.session['user']}
    
    return render_to_response('home.html', args,context_instance=RequestContext(request))

def register(request):
    args = {}

    if "username" in request.POST and "password" in request.POST and "fullname" in request.POST:
        hashedPW = hashlib.md5(request.POST['password']).hexdigest()
        new_user = Author(username=request.POST['username'],password=hashedPW,fullname=request.POST['fullname'])
    else:
        return redirect('/')
    try: 
        user = Author.objects.get(username=new_user.username)
    except Author.DoesNotExist:
        verif_num = hashlib.md5((random.random()*1000)+str(new_user.username+new_user.password+new_user.fullname)).hexdigest()[0:16]
        new_user.verif_number = verif_num
        #send confirmation email with verification #
        link = str(request.get_host() +'/verify/'+str(new_user.verif_number))+'/'
        try:
            send_mail('Welcome to Wuphf, '+new_user.fullname, 'Click the link to verify! '+link,'wuphf@wuphf.com',[new_user.username],fail_silently=False)
        except Exception:
            print "Error sending verification email..."
            args = {'success':False} 
        else:
            args = {'success':True}
        new_user.save()
    else:
        args = {'success':False}

    #validate fields
    #send confirmation email
    #check for matches on username OR email 
    return redirect('/')

def verify(request):
    args = {}
    if 'verify_failed' in request.session:
        args = {'verify_failed':request.session['verify_failed']}
        #render a verify form 
        return render_to_response('verify.html', args,context_instance=RequestContext(request))

    if 'verif_num' in request.POST:
        return redirect('/verify/'+str(request.POST['verif_num']+'/'))
    else:
        return render_to_response('verify.html', args,context_instance=RequestContext(request))

#this is the function called when you click the verify link in your email
def verify_noform(request):
    args = {}
    regexp = re.compile('[a-zA-Z0-9]{16,16}')
    
    #get number from URL
    
    verif_num = request.path[8:len(request.path)-1]
    #urlpatterns already checks this in a way, but we'll check it again anyway.
    if regexp.match(verif_num):
        #see if we can find the token in the database, and mark the user verified
        try:
            user = Author.objects.get(verif_number=verif_num)
        except Author.DoesNotExist:
            #ut ohs!
            print 'Can\'t find user!'
            pass            
        else:
            #mark user as verified, redirect to homepage
            user.verified = True
            user.save()
            request.session['user'] = user.fullname
            return redirect('/home/')
    else:
        print 'Invalid verify_number'

    return render_to_response('home.html', args,context_instance=RequestContext(request))


def login(request):
    if "user" in request.session:
        del request.session['user']

    if 'username' in request.POST and 'password' in request.POST:
        if request.POST['username'] != '' and request.POST['password'] != '':
            username = request.POST['username']
            password = hashlib.md5(request.POST['password']).hexdigest()
            try:
                user = Author.objects.get(username=username, password=password)
            except Author.DoesNotExist:
                return redirect('/')
            else:
                if user.verified is True:
                    request.session['user'] = user.fullname
                    request.session['userid'] = user.id
                    return redirect('/home')
                else:
                    request.session['verify_failed'] = True
                    return redirect('verify')

    return redirect('/')

def logout(request):
    if "user" in request.session:
        del request.session['user']

    return redirect('/')
