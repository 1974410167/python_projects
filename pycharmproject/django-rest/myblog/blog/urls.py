from django.urls import path,include

from . import views



urlpatterns = [
    path('get_all_data/', views.get_all_data),
    path('<int:age>/',views.my_name,{'gender':'Famale'},name='blog-age'),
    path('<int:year>/<int:month>/<int:day>/',views.birthday,name='blog-year-month-day'),

]