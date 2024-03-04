from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def v(request):
    return HttpResponse('Site 1')