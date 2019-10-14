from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from demo import models

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def hello_world(request):
    return HttpResponse("Hello World")


# 对送骨保密画面
def index(request):
    user_info = models.UserInfoDemo.objects.all()
    return render(request, 'index.html',
                  {
                      'user_info': user_info
                  }
                  )


# データ保存操作
@csrf_exempt
def data_add(request):
    userid = request.POST['userId']
    username = request.POST['userName']
    password = request.POST['passWord']
    userage = request.POST['userAge']
    usermail = request.POST['userMail']

    # 方法1
    # models.UserInfoDemo.objects.create(userId=userid)

    # 方法2
    info = models.UserInfoDemo()
    if len(userid) > 0:
        print("id不是null")
        info.userId = userid
    info.userName = username
    info.passWord = password
    info.userAge = userage
    info.userMail = usermail

    info.save()

    return HttpResponseRedirect("/demo/index")


# データ削除操作
@csrf_exempt
def data_delete(request):
    userid = request.POST['userId']

    # 方法1
    models.UserInfoDemo.objects.filter(userId=userid).delete()

    # 方法2
    # info = models.UserInfoDemo()
    # if len(userid) > 0:
    #     print("id不是null")
    #     info.userId = userid;
    #
    # info.delete()

    return HttpResponseRedirect("/demo/index")
