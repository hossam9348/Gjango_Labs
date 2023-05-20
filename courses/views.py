from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect


# Create your views here.
def coursesList(request):
    context={}
    # context['pagename']='Courses\nList'
    context['courses']=['course1','course2','course3']
    return  render(request,'courseList.html',context)

def courseAdd(req):
    return render(req,'addCourse.html')

def courseUpdate(req,ID):
    return  HttpResponseRedirect('/courses')

def courseDelete(req,ID):
    return  HttpResponseRedirect('/courses')
