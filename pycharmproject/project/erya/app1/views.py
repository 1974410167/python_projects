from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):

    s = '<h1>success</h1>'

    return HttpResponse(s)
