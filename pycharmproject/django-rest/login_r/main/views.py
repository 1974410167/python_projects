from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,response
from .import models
from . import forms


def login(request):

    if request.session.get('is_login',None):
        return redirect(reverse('main_urls:index_url'))

    if request.method == 'POST':
        login_form = forms.userforms(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            name = login_form.cleaned_data.get('name')
            password = login_form.cleaned_data.get('password')

            try:
                user_t = models.user.objects.get(name=name)
                user_pawd_t = user_t.password
                print(request.session)
                request.session['is_login'] = True
                request.session['name'] = name
                request.session['password'] = password
                print(request.session)
                for i in request.session.items():
                    print(i)

                return redirect('main_urls:index_url')
            except:
                message = '用户或密码错误'
                return HttpResponse(message)
    else:
        form = forms.userforms()
        return render(request,'name.html',{'form':form})

def index(request):

    print(request.session)
    name = request.session.get('name',None)
    message = f'{name}登陆成功！'
    rep = HttpResponse(message)
    rep.set_cookie('hhhhhhhhhhhh','mmmmmmmmmmm')
    print(rep.cookies)
    return rep

def register(request):

    if request.method == 'POST':
        register_form = forms.userforms(request.POST)
        message = ''
        if register_form.is_valid():
            username = register_form.cleaned_data.get('name')
            password = register_form.cleaned_data.get('password')
            try:
                t = models.user.objects.get(name=username)
                message = '用户名已经存在'
                return HttpResponse('用户名已经存在')
            except:

                register_form.save()
                return redirect('main_urls:login_url')

    else:
        form = forms.userforms()
        return render(request, 'register.html', {'form': form})

    return HttpResponse('注册')




