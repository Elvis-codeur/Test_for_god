import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def number_view(request):
    return HttpResponse('The magic number is {}'.format(os.getenv('number')))