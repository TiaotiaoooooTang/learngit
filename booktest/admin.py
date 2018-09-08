from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bread']   # 指定显示两列
    list_per_page = 2      # 指定显示多少条数据
    # actions_on_bottom = True

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hbook', 'read']
    list_filter = ['hbook', 'hgender']
    search_fields = ['hname']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)









#
# #
# with open('/home/python/Desktop/坐标.txt', 'rb') as f:
#     content = f.read().decode().split(' ')
#     # print(content)
# list1 = []
# for i in content:
#     # print(list1.index(i))
#     k = content.index(i)
#     if k % 35 == 0:
#         list1.append(i)
# print(list1)

