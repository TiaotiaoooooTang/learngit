from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
#     正则给组起名
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # django中查询请求体中的字符串参数    http://127.0.0.1:8000/query/?a=1&b=2&c=3&c=4
    url(r'query/$',views.query_data),
    # 查询form表单数据
    url(r'^form_data/$',views.form_data),
    # 查询请求体中的非表单数据
    url(r'^json_data/$',views.json_data),
    # 演示Django中构造响应对象
    # /get_response/
    url(r'^get_response/$',views.get_response),
    # 返回json 数据
    url(r'^get_json/$',views.get_json),
    # 页面重定向
    url(r'^redirect/$',views.redirect_demo)
# day01
# ==============================================================================================================


]