from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import CreateView

class TraineeGErtnic(CreateView):
    model = Trainee
    fields='__all__'

# Create your views here.
@login_required
def traineesList(request):
    context={}
    # context['pagename']='Trainees\nList'
    context['trainees']= Trainee.objects.all()
    return  render(request,'traineeList.html',context)



@login_required
def traineeAdd(req):
    context = {}
    form=Add()
    context['form']=form
    if(req.method=='GET'):
        return render(req,'addTrainee.html',context)
    else:
        #insert trainee in model task
        #get data
        form = Add(req.POST)
        if(form.is_valid()):
            # form.save()
            nameinput=req.POST['name']
            Trainee.objects.create(name=nameinput)
            return HttpResponseRedirect('/trainees')
        # nameinput=req.POST['name']
        #create object from task mode
        # Trainee.objects.create(name=nameinput)

def traineeUpdate(req,ID):
    context={}
    form=Update()
    context['form']=form
    context['trainee']=Trainee.objects.get(id=ID)
    if(req.method=='GET'):
        return render(req,'updateTrainee.html',context)
    else:
        form = Update(req.POST)
        if(form.is_valid()):
          nameinput=req.POST['name']
          Trainee.objects.filter(id=ID).update(name=nameinput)
          return HttpResponseRedirect('/trainees')

def traineeDelete(req,ID):
    Trainee.objects.filter(id=ID).delete()
    return  HttpResponseRedirect('/trainees')



