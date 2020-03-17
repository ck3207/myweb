from django.shortcuts import render
from django.template.loader import get_template
from posts import models
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = get_template("post/index.html")
    posts = models.Post.objects.filter(enabled=False).order_by('-pub_time')[:30]
    # posts = models.Post.objects.filter(nickname="admin").order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = "Every info needs to be write down..."
    if user_id:
        try:
            mood = models.Mood.objects.get(mood=user_mood)
            post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            message = "Save Successfully. Please edit your password [{0}], " \
                      "info would be display when has been verified.".format(user_pass)
        except Exception as e:
            message = str(e)
    return render(request, 'post/index.html', locals())


