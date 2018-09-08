from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')


def say(request):
    return HttpResponse('say')


def sayhello(request):
    return HttpResponse('sayhello')