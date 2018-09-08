from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse , HttpResponseRedirect

# Create your views here.
def weather(request,year , city):
    print(city)
    print(year)
    return HttpResponse('OK')

# django中获取请求提中的字符串参数    http://127.0.0.1:8000/query/?a=1&b=2&c=3&c=4
# debug
def query_data(request):  # GET
    a = request.GET.get('a')  # a=1
    b = request.GET.get('b')  # b=2
    c = request.GET.get('c')  # c=4   若传入的url地址中有名字相同的参数，则默认返回最后一个值

    c_list = request.GET.getlist('c')   #  c=[3,4] 使用getlist属性可返回一个列表

    return HttpResponse('OK')

# 演示Django中获取请求体中的表单类型数据
# postman debug
def form_data(request):   # POST
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse('OK')

# 演示Django中获取请求体中的非表单类型数据
def json_data(request):   # body
    req_data = request.body    # bytes
    import json
    json.dump(dict)      # 将python字典转换成json格式
    json.load(str)   # 将json 字符串转换成python 字典
    req_dict = json.loads(req_data.decode())   # 解码
    return HttpResponse('OK')

# 演示Django中构造响应对象
# /get_response/
def get_response(request):
    response = HttpResponse('hello itcast', content_type = 'text/html',status=404)
    # 设置响应头内容
    response['Name'] = 'Itcast'
    return response

# 返回json数据
def get_json(request):
    res_dic = {
        'name':'itheima',
        'age':11
    }
    return JsonResponse(res_dic)


# 页面重定向
def redirect_demo(request):
    return redirect('/get_response/')

# day01
# ==============================================================================================================================
