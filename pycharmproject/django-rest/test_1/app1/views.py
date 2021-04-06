from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.viewsets import GenericViewSet
from .models import User,Token



class testview(GenericViewSet):

    def get(self,request,*args,**kwargs):

        return HttpResponse("GET请求")

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST请求")


