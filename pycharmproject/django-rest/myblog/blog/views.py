from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from .import models

from .forms import NameForm

def my_name(request,age,gender):
    message='嘿嘿'
    html=f"<html><body>my name is {message},age is {age},gender is {gender}</body></html>"
    return HttpResponse(html)

def birthday(r,year,month,day):
    message='嘻嘻'
    html=f"<html><body>my name is {message},birthday is {year}-{month}-{day}</body></html>"
    return HttpResponse(html)

def get_all_data(r):
    a=models.Student.objects.all()
    html=f"<html><body>{a[0].name}</body></html>"
    return HttpResponse(html)

def thanks(r):
    return HttpResponse('redirect successful !!!')


def index(r):
    if not r.session.get('is_login',None):
        return redirect('/your_name/')

def get_name(request):
    # if this is Post request we need to proecss the form data
    if request.method == 'POST':
        # reate a form instance and populate is with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return redirect('/thanks/')
    else:
        form = NameForm()
    return render(request,'name.html',{'form':form})
