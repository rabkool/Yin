## Django

#### 基础命令

- starproject # 创建一个Django项目
- startapp # 创建一个Django应用
- check # 校验项目完整性
- runserver # 本地简易运行Django项目
- shell # 进入Django项目的Python Shell环境
- test # 执行Django测试

#### DB关联命令

- makemigrations # 创建模型变更的迁移文件
  - 模型层
- dumpdate # 把DB数据导出到文件
- loaddata # 把文件数据导入到DB



#### Django项目目录

- 初始化必备文件
  - 项目管理文件: manage.py
  - 配置文件: settings.py
  - 路由文件配置文件: urls.py 
  - Django作为wsgi应用需要的文件: wsgi.py 
  - 存放html: templates



#### Django应用目录介绍

- 初始化必备文件
  - 定义Admin模块管理: admin.py
  - 声明应用: apps.py
  - 定义应用模型: models.py
    - 模型层
      - 位于Django视图层和DB之间
      - Python对象和DB表之间的转换
  - 测试应用: tests.py
  - 视图处理: views.py
  - 管理应用路由(需自己创建): urls.py



#### 增删改查

- 增

  - ```
    userid = request.POST['userId']
    models.UserInfoDemo.objects.create(userId=userid)
    ```

  - ```
    userid = request.POST['userId']
    info = models.UserInfoDemo()
    info.userName = username
    info.save()
    ```

- 删

  - ```
    userid = request.POST['userId']
    models.UserInfoDemo.objects.filter(userId=userid).delete()
    ```

  - ```
    userid = request.POST['userId']
    info = models.UserInfoDemo()
    info.delete()
    ```

- 改

  - ```
    userid = request.POST['userId']
    models.UserInfoDemo.objects.filter(userId='1').update(passWord='111')
    ```

  - ````
    userid = request.POST['userId']
    info = models.UserInfoDemo.objects.get(userId='1')
    info.passWord = '111'
    info.save()
    ````

- 查

  - ```
    #全部查询
    userid = request.POST['userId']
    models.UserInfoDemo.objects.all()
    ```

  - ```
    #查询第一个数据
    userid = request.POST['userId']
    models.UserInfoDemo.objects.all()[0]
    ```

  - ```
    #只取userId列
    userid = request.POST['userId']
    models.UserInfoDemo.objects.all().values('userId')    #只取user列
    ```

  - ```
    #取出userId和password列，并生成一个列表
    models.UserInfoDemo.objects.all().values_list('userId','password')  
    ```

  - ```
    models.UserInfo.objects.get(id=1)
    ```
#### 画面URL
 - http://127.0.0.1:8000/demo/index/

    

````

````