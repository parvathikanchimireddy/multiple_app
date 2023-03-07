from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first_app2(request):
    return HttpResponse('<h3>This is first function in app2</h3>')
def second_app2(request):
    return HttpResponse('<h3>This is second function in app2</h3>')