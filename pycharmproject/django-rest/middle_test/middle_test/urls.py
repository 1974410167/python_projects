"""middle_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,include
from mid1 import views as mid_views

# from ..mid1 import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('midtest/', mid_views.mid_test),
    path('pub/',mid_views.PublishList.as_view()),
    # path('detail/<int:pk>', mid_views.DetailPublish.as_view(),name='detail'),
    path('',include('mid1.urls')),

]
