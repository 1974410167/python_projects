

from django.urls import path
from . import views

app_name = "HaoYuan"
urlpatterns = [
    path('user/',views.user),
    path('requ/',views.TestView.as_view()),
    path('te_test/', views.te_test),
    path('html1/', views.html1),
    path('abc/', views.abc),
    path('your-name/', views.get_name),
    path('my_form/',views.student_views),
    path('pra/',views.practice_view,name = "pra_url"),
    path('search/',views.search_view,name="search_id"),
    path('detail/<int:my_id>/', views.detail_view,name="detail_url"),
    path('search/<str:name>/', views.name_view,name = "search_url"),

    ## test view
    path('curr_time/', views.current_view,name = "curr_url"),
    path('test/',views.redict_test)

]