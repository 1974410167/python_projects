from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .serializers import *
from rest_framework import viewsets,request
from .models import Student,user
from rest_framework.views import APIView
from rest_framework.response import Response

def get_image(request,image):
    base = 'D:/pycharm/pycharmproject/django-rest/DRF/DRF/root_file/uploads/'
    url = base+image
    return HttpResponse(url)


# 好用
class StudentVs(viewsets.ModelViewSet):

    serializer_class = StudentSer
    queryset = Student.objects.all()

class UserVs(viewsets.ModelViewSet):

    serializer_class = UserSer
    queryset = user.objects.all()


class StudentAPIView(viewsets.ViewSet):

    def get(self,request):
        """
        处理业务与数据库的交互
        :param request:
        :return:
        """

        queryset = Student.objects.all()
        serializer = StudentSer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):

        s = request.data
        print(type(s))
        print(s)
        ob = StudentSer(data=s)
        if ob.is_valid():
            v = Student()
            v.name = ob.validated_data['name']
            v.age = ob.validated_data['age']
            v.save()
        else:
            return HttpResponse("please input valid data!")
        return HttpResponse("successful!!")

