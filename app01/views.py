from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

# def login(request):
#     if request.method == "GET":
#         return render(request,"login.html")
#     elif request.method == "POST":
#         u = request.POST.get("user")
#         p = request.POST.get("pwd")
#         if u == "yanzhuang" and p == "123":
#             return redirect("/admin/")
#         else:
#             return render(request,"login.html")
#     else:
#         return redirect("/admin/")
from django.views import View

USER_DICT = {
    "1":{"name":"root1","email":"123","tel":"123124"},
    "2":{"name":"root2","email":"123","tel":"123124"},
    "3":{"name":"root3","email":"123","tel":"123124"},
    "4":{"name":"root4","email":"123","tel":"123124"},
}

def index(request):
    return render(request,"index.html",{"user_dict":USER_DICT})


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":

        obj = request.FILES.get("fafafa")

        import os
        file_path = os.path.join("upload",obj.name)

        f = open(file_path,mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()
        return render(request, "login.html")
    else:
        return redirect("/admin/")

class Home(View):


    def dispatch(self, request, *args, **kwargs):
        "类似装饰器的作用"
        print("before")
        #调用父类的dispatch方法
        result = super(Home,self).dispatch(request,*args,**kwargs)
        print("after")
        return result

    def get(self,request):
        print(request.method)
        return render(request,"home.html")

    def post(self,request):
        print(request.method)
        return render(request,"home.html")


def detail(request,*args,**kwargs):
    # return HttpResponse(nid)

    info = USER_DICT[kwargs.get("nid")]
    return render(request,"detail.html",{"user_info":info})
