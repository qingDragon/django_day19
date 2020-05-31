from django.contrib import admin
from django.urls import path,re_path

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/',views.login),
    # path('home/',views.Home.as_view()),
    path('index/',views.index),
    # re_path('index/(\d+)/',views.index,name= "index"),
    # # re_path('detail-(\d+).html',views.detail),  #正则匹配的时候需要导入re_path包
    # re_path('detail-(?P<nid>\d+)-(?P<uid>\d+)',views.detail) , #分组匹配
    path('orm/',views.orm),
    path('userinfo/',views.user_info),
    re_path('userdetail-(?P<nid>\d+)/',views.user_detail),
    re_path('userdel-(?P<nid>\d+)/',views.user_del),
    re_path('useredit-(?P<nid>\d+)/',views.user_edit),
]