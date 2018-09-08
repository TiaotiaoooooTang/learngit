from django.conf.urls import url
from . import views
# from .views import index


# http://127.0.0.1:8000/users/index   匹配index
urlpatterns = [
    url(r'^index/$',views.index),     # url配置项
    # url(r'^index/$', index),
    url(r'^say/$', views.say),
    url(r'^sayhello/$',views.sayhello)
]