from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def first(request):
    return render(request,'monkey/first.html')

def capl_des(request):
    return render(request, 'monkey/capl_des.html')

def capl_des_handle(request):
    base_text = '''G_TST_TestStepAddPurpose("tempStr1");'''
    input_text = request.POST.get('input')
    if input_text:
        text_spilt = input_text.split('\n')
        out_text = '\n'.join(text_spilt)

        text_output = base_text.replace("tempStr1", out_text)
        print(text_output)
        context = {'text_intput':input_text,'text_output':text_output}
        return render(request, 'monkey/capl_des.html', context)
    else:
        context = {'text_intput':input_text,'text_output':"input is NULL"}
        return render(request, 'monkey/capl_des.html', context)

def html_to_doors(request):
    return render(request,'monkey/html_to_doors.html')

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
        return render(request, 'monkey/html_to_doors.html', context)
    else:
        context = {'text_intput':"输出为空！",'text_output':"输出为空！"}
        return render(request, 'monkey/html_to_doors.html', context)