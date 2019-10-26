from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from demo import models

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

# 分页插件
from django.core.paginator import Paginator


def hello_world(request):
    return HttpResponse("Hello World")


# 画面
def index(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print(page)

    # 全部查询
    detail_info = models.UserInfoDemo.objects.all()

    # 分页判断 10: 显示条数
    paginator = Paginator(detail_info, 10)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, 'index.html',
                  {
                      'user_info': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page
                  }
                  )


# データ保存操作
@csrf_exempt
def data_add(request):
    user_id = request.POST['userId']
    user_name = request.POST['userName']
    user_password = request.POST['passWord']
    user_age = request.POST['userAge']
    user_mail = request.POST['userMail']

    # 方法1
    # models.UserInfoDemo.objects.create(userId=userid)

    # 方法2
    info = models.UserInfoDemo()

    info.userId = user_id
    info.userName = user_name
    info.passWord = user_password
    info.userAge = user_age
    info.userMail = user_mail

    info.save()

    return HttpResponseRedirect("/demo/index")


# データ削除操作
@csrf_exempt
def data_delete(request):
    user_id = request.POST['userId']

    # 方法1
    models.UserInfoDemo.objects.filter(userId=user_id).delete()

    # 方法2
    # info = models.UserInfoDemo()
    #
    # info.userId = userid;
    #
    # info.delete()

    return HttpResponseRedirect("/demo/index")


# update
@csrf_exempt
def update(request):
    # userid = request.POST['userId']
    # username = request.POST['userName']
    models.UserInfoDemo.objects.filter(userId=1).update(userName="user",
                                                        passWord="123",
                                                        userAge="11",
                                                        userMail="123321"
                                                        )
    return HttpResponseRedirect("!!")


# select
def select(request):
    user_id = request.GET['userId']
    # 全部查询
    user_select = models.UserInfoDemo.objects.get(userId=user_id)
    return render(request,
                  "index.html",
                  {
                      "user_select": user_select
                  }
                  )
