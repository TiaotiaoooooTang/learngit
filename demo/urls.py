
from django.conf.urls import url,include
from django.contrib import admin


# http://127.0.0.1:8000/users/index   匹配users
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('users.urls')),
    url(r'^',include('request_vs_response.urls'))
]
