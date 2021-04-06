from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib import sessions
class auth_1(BaseAuthentication):
    pass

class mypermission(object):
    def has_permission(self,request,view):
        if request.Student.age<18:
            return False
        return True


class Student_views(APIView):
        # permission_classes = [mypermission,]
        def get(self, request):
            """
            处理业务与数据库的交互
            :param request:
            :return:
            """
            token = request.GET.get("token")
            s = request.query_params.get("token")
            print(token)
            print(s)
            return HttpResponse('SS')

            # if token:
            #     try:
            #         token_obj = token_1.objects.get(token=token)
            #         name = token_obj.student.name
            #         age = token_obj.student.age
            #         score = token_obj.student.score
            #         res = HttpResponse(f"{name},{age}")
            #         res.set_cookie('hello','world')
            #         return res
            #
            #     except :
            #         return HttpResponse("token不合法")
            # else:
            #     return HttpResponse("未带token,禁止访问")



            return HttpResponse(f"get请求{pk}")

        def post(self, request):
            import json

            # 仅仅支持x-www-form-urlencoded模型，类型为QueryDict
            # s = request.data
            # 仅仅支持x-www-form-urlencoded模型，类型为QueryDict
            # # m = request.POST
            # # print(type(m))
            # # print(m.values())
            #
            # print(type(s))
            # print(s['score'])
            # print("==========")
            # # json数据从request.body中拿到，并loads序列化
            # n = request.body
            # print(n)
            # print(type(n))
            # print(json.loads(n))

            ## 这里加入rest_framework的解析器,自动解析x-www-form-urlencoded和json
            r = request.data
            print(r)
            return HttpResponse("successful!!")



