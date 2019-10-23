from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserInfo

# Create your views here.
def user_add(request):
    #添加用户
    if request.method == 'GET':
        #拿页面
        return render(request, 'index/user_add.html')
    elif request.method == 'POST':
        #添加用户
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        UserInfo.objects.create_user(username=username, password=password, email=email)

        return HttpResponseRedirect('/index/add')

def user_show(request):
    #显示所有用户
    all_user = UserInfo.objects.all()
    return render(request, 'index/user_show.html', locals())
















