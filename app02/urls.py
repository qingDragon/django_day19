from django.contrib import admin
from django.urls import path,re_path

from app02 import views

urlpatterns = [

    path('login/',views.login),

]