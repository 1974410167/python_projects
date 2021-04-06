from django.shortcuts import render,HttpResponse
from .models import Publish
# Create your views here.


def mid_test(request):

    print('执行视图mid_test')

    return HttpResponse('200,ok')

from django.views.generic import ListView,DetailView


class PublishList(ListView):
    model = Publish
    context_object_name = 'my_publish_list'
    template_name = 'publish.html'
    paginate_by = 1


class DetailPublish(DetailView):
    context_object_name = 'detailpublish'
    queryset = Publish.objects.all()
    template_name = 'detail.html'

def htr(request):

    t1 = request
    print("*"*30)

    print(t1)
    print(type(t1))
    print(t1.path)
    print(t1.method)
    print(t1.encoding)
    print(t1.headers)
    print(t1.scheme)
    print("*"*30)

    return HttpResponse("it is ok")