from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404,redirect
import json
from django.views import View
from . import models
from django.urls import reverse
# Create your views here.


def user(r):
    user_list=["小红","小明"]
    return HttpResponse(json.dumps((user_list),ensure_ascii=False))

class TestView(View):

    def get(self,*args,**kwargs):
        return HttpResponse("Get")
    def post(self,*args,**kwargs):
        return HttpResponse("Post")
    def put(self,*args,**kwargs):
        return HttpResponse("Put")

def te_test(r):
    a=r.user
    return render(r,"te_test.html",context={'a':a})
def abc(r):
    return render(r,"form.html",{})

def html1(r):
    list=[1,2,3,4,5,6]
    return render(r,"html1.html",context={'list':list})

from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(models.Student.get_absolute_url)
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

from .forms import Student_form,practice_form


def student_views(request):
    my_form = Student_form()
    if request.method == "POST":
        my_form = Student_form(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            my_form.save()
    context = {
        'form' : my_form
    }
    return render(request,'form.html',context)

def practice_view(request):
    if request.method == 'POST':
        form = practice_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('HaoYuan:search_url'))
    else:
        form = practice_form()

    return render(request, 'name.html', {'form': form})

def search_view(request):


    target = models.Student.objects.all()
    # target = get_object_or_404(models.Student,id=my_id)
    # target = models.Student.objects.all()
    context = {
        'abc':target
    }
    return render(request,'search.html',context)

def name_view(request,name):

    t = name

    context = {
        "t":t
    }
    return render(request,'name_view.html',context)


def detail_view(request,my_id):

    target = get_object_or_404(models.Student,id = my_id)

    context = {
        "detail":target
    }

    return render(request,"detail.html",context)

import datetime
def current_view(request):

    now = datetime.datetime.now()

    html = f"<html><body>it is now {now}</body></html>"

    return HttpResponse(html)

def redict_test(request):

    return HttpResponseRedirect(reverse("HaoYuan:search_id"))

