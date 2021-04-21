# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    texts = ['Lorem ipsum dolor sit amet', 'Curabitur blandit dapibus']
    context = {
        'title': 'django e-commerce',
        'texts': texts
    }
    return render(request,'index.html', context)