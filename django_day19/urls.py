"""django_day19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path,include

import app01
import app02
from app01 import views

urlpatterns = [
    #多个app的路由分发
    path('cmdb/', include("app01.urls")),
    path('monitor/', include("app02.urls")),

]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/',views.login),
#     path('home/',views.Home.as_view()),
#     path('index/',views.index),
#     # re_path('detail-(\d+).html',views.detail),  #正则匹配的时候需要导入re_path包
#     re_path('detail-(?P<nid>\d+)-(?P<uid>\d+)',views.detail)  #分组匹配
# ]