from django.contrib import admin

from django.urls import path
from mid1 import views as mid_views

app_name = 'mid1'
urlpatterns = [
    path('detail/<int:pk>', mid_views.DetailPublish.as_view(),name='detail'),
    path('htr/',mid_views.htr,name = 'htr')
]
