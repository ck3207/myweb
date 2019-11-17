from django.shortcuts import render
from django.template.loader import get_template
from posts import models
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = get_template("post/index.html")
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    return render(request, 'post/index.html', locals())

