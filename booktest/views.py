from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.generic import View
from .models import BookInfo
# Create your views here.

# 使用Django自定义RestAPI
class BookListView(View):
    def get(self,requestt):
        books = BookInfo.objects.all()
        book_li = []
        for book in books:
            # 获取图书信息
            book_dict = {
                'id': book.id,
                'btitle': book.bpub_date,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            }
            book_li.append(book_dict)
        return JsonResponse(book_li,safe=False)



