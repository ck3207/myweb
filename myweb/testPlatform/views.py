import os

from django.shortcuts import render

# Create your views here.

PREFIX = 'testPlatform'
def get_homepage(request):
    return render(request, os.path.join(PREFIX, 'index.html'), locals())


def get_func(request):
    request.GET['']
    return None