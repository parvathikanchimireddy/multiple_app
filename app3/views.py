from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first_app3(request):
    return HttpResponse('<h1><marquee>This is first function in app3</marquee></h1>')
def second_app3(request):
    return HttpResponse('<h1><marquee>This is second function in app3</marquee></h1>')