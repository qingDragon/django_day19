from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


from django.views import View

from app01 import models


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        print(u,p)
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        print(obj)
        if(obj):
            return redirect("/cmdb/index/")
        else:
            return render(request, "login.html")
    else:
        return redirect("/index/")

def index(request):
    return render(request,"index.html")


def orm(request):
    "数据库增删改查操作"
    #增
    #models.UserInfo.objects.create(username="root",password='123')
    # models.UserInfo.objects.filter(id='3').delete()
    # obj = models.UserInfo(username='yanzhuang',password='123123')
    # obj.save()
    # obj2 = models.UserInfo(username='guyang',password='admin')
    # obj2.save()
    #删
    models.UserInfo.objects.filter(id='4').delete()

    #查

    # result = models.UserInfo.objects.all() #result 的类型是Queryset，Django中自带的，看成列表去处理
    # for row in result:
    #     print(row.id,row.username,row.password)
    #
    # #更新
    # models.UserInfo.objects.filter(id='5').update(username='zhangshuo')
    #
    return HttpResponse("orm")