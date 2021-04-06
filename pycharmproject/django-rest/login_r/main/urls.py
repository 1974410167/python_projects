from django.urls import path,include

from . import views



app_name = 'main_urls'

urlpatterns = [
    path('login/', views.login,name='login_url'),
    path('index/', views.index,name='index_url'),
    path('register/', views.register,name='register_url'),
]