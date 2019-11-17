"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from analysis import views as v
from posts import views as vp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', v.homepage, name='homepage'),
    path('', vp.index),
    re_path('^label/$', v.get_labels, name='lable'),
    path('lable/detail/', v.get_lable_detail, name='lable_detail'),
    path('detail/<str:table_name>', v.get_detail, name='detail'),
]
