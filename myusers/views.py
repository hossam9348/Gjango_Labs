from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from  django.contrib.auth import login as authlogin,authenticate
# Create your views here.
def Login(req):
    if (req.method == 'GET'):
        return render(req,'login.html')
    else:
        u= Myuser.objects.filter(username=req.POST['username'],Password=req.POST['password'])
        authuser=authenticate(username=req.POST['username'],password=req.POST['password'])
        if(len(u)>0 and authuser is not None):
                req.session['username']=u[0].username
                #autologin admin pane
                authlogin(req,authuser)
                return  HttpResponseRedirect('/trainees')
        else:
               context={}
               context['msg']='ivalid user name or password'
               return render(req, 'login.html',context)


def Reg(req):
    if(req.method=='GET'):
        return render(req,'register.html')
    else:
        print(req.POST)
        Myuser.objects.create(name=req.POST['name'],Password=req.POST['password'],username=req.POST['username'],age=req.POST['age'])
        User.objects.create_superuser(username=req.POST['username'] ,password=req.POST['password'], email=req.POST['email'], is_active=True)
        return HttpResponseRedirect('/users/login')
def Logout(req):
    req.session.clear()
    return HttpResponseRedirect('/users/login')