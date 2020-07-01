
#coding=utf-8
from hashlib import sha1

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def First(request):
    return render(request,'df_user/First.html')
def register(request):
    return render(request,'df_user/register.html')
def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    if upwd!=upwd2:
        return redirect('/user/register')
    # #密码加密
    # s1 = sha1()
    # s1.update(upwd.encode('utf-8'))
    # upwd3 = s1.hexdigest()

    #创建对象
    user = UserInfo()
    user.uname = uname
    #user.upwd = upwd3
    user.upwd = upwd
    user.uemail = uemail
    user.save()
    return redirect('/user/login')

#检测注册页面用户名是否存在
def register_exist(request):
    uname = request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    print('count')
    print(count)
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    print("login...")
    return render(request,'df_user/login.html',context)

def login_handle(request):

    post = request.POST
    uname = post.get('username')
    upwd=post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    print("用户名：%s 密码：%s"%(uname,upwd))
    if len(users)== 1:

        # s1 = sha1
        # s1.update(upwd.encode('utf-8'))
        # if s1.hexdigest() == users[0].upwd:
        if upwd == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)

def info(request):
    user_email = UserInfo.objects.get(id = request.session['user_id']).uemail
    context ={'title':'用户中心',
              'user_email':user_email,
              'user_name':request.session['user_name']}

    return render(request,'df_user/user_center_info.html',context)

def capl_des(request):
    return render(request, 'df_user/capl_des.html')

def capl_des_handle(request):
    base_text = '''G_TST_TestStepAddPurpose("tempStr1");'''
    input_text = request.POST.get('input')
    if input_text:
        text_spilt = input_text.split('\n')
        out_text = '\n'.join(text_spilt)

        text_output = base_text.replace("tempStr1", out_text)
        print(text_output)
        context = {'text_intput':input_text,'text_output':text_output}
        return render(request, 'df_user/capl_des.html', context)
    else:
        context = {'text_intput':input_text,'text_output':"input is NULL"}
        return render(request, 'df_user/capl_des.html', context)

def html_to_doors(request):
    return render(request,'df_user/html_to_doors.html')

def html_to_doors_handle(request):
    from .myApp.html_to_doors_html import HtmlToDoors
    from lxml import etree

    file_obj = request.FILES.get('file', None)
    if file_obj:
        app = HtmlToDoors()
        strr = file_obj.read()
        html = etree.fromstring(strr, etree.HTMLParser())
        app.start_thansform(html)
        print(type(html))

        # print(file_obj.name)
        # print(file_obj.size)
        # with open('static/images/' + file_obj.name, 'wb') as f:
        #     for line in file_obj.chunks():
        #         f.write(line)
        # f.close()
        context = {'text_intput':app.doors_text_output,'text_output':app.capl_text_output}
        return render(request, 'df_user/html_to_doors.html', context)
    else:
        context = {'text_intput':"输出为空！",'text_output':"输出为空！"}
        return render(request, 'df_user/html_to_doors.html', context)
