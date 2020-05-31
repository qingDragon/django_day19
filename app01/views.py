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

def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        print(user_list.query)#打印sql语法
        return render(request,"user_info.html",{'user_list':user_list})
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        models.UserInfo.objects.create(username=u,password=p)
        return redirect('/cmdb/userinfo/')
def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request,'user_detail.html',{'obj':obj})

def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/userinfo/')

def user_edit(request, nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html',{'obj': obj})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/userinfo/')

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