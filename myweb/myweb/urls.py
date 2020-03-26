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
    path('', v.homepage, name='homepage'),
    re_path('^labels/$', v.get_labels, name='lables'),
    path('labels/detail/<str:table_name>', v.get_detail, name='detail'),
    # path('orthogonalArray/', v.get_orthogonal_array_info, name='orthogonal_array'),
    path('addHost/', v.add_host, name='addHostHtml'),
    path('addHost/result.html', v.add_host_detail, name='addHostDetail'),
    path('del/', v.del_data, name='del_data'),
    path('addHostDetail/', v.add_host_detail, name='addHostDetail2'),
    re_path('^autoDeploy/$', v.autoDeploy, name='autoDeploy'),
    path('autoDeploy/light/', v.get_pkgs, name='autoDeploy_light'),
    path('autoDeploy/light/deploy-on-light/', v.deploy_on_lihgt, name='deploy_on_light'),
    path('light/', v.get_pkgs, name='autoDeploy-light'),
    path('addHost/query_hosts.html', v.query_hosts, name='query_hosts'),
]
