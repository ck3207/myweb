import json
import os

from django.shortcuts import render, redirect
from django.conf import settings
from .models import LableNum, LableDetail, Tools, Servers, ConfigTable
# from .orthogonalArray.config import Config as c
from .conf.config import ConfigInfo
from .utilities.deploy_on_light import DeployOnLight
from .utilities.download_from_pkg import Download
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    all_tools = Tools.objects.all()
    tools_num = len(all_tools)
    return render(request, 'home.html', locals())


def get_labels(request):
    all_tables = LableNum.objects.all()
    tables_num = len(all_tables)
    return render(request, 'labels.html', locals())


def get_detail(request, table_name="acct_wt_user_money_in_out"):
    detail = LableDetail.objects.filter(table_name=table_name).order_by("column_name", "interval_type")
    label_num = LableNum.objects.get(table_name=table_name)

    return render(request, 'detail.html', locals())


# def get_orthogonal_array_info(request):
    # config = Config(config_file="conf/conf.ini")
    # factor, col, split = config.get_config()
    # col = ",".join(col)
    # return render(request, 'orthogonal_array.html', locals())


def add_host(request):
    """Add host page."""
    return render(request, 'add_host.html', locals())


@csrf_exempt
def add_host_detail(request):
    """Add host data commit."""
    address = request.POST['hostAddress']
    port = request.POST['port']
    user = request.POST['username']
    password = request.POST['password']
    try:
        Servers.objects.create(address=address, port=port, user=user, password=password)
        return redirect("addHost/query_hosts.html")
        # return HttpResponse("Insert data successfully.")
    except Exception as e:
        return HttpResponse('Insert data failured.Probably data have already existed.')

def del_data(request):
    db_info = {'servers': Servers}
    db_name = request.GET['db_name']
    db_info.get(db_name).objects.all().delete()
    return HttpResponse('Del Data Successfully.')

@csrf_exempt
def query_hosts(request):
    host_info = Servers.objects.all()
    return render(request, 'query_hosts.html', locals())

def autoDeploy(request):
    datas = Servers.objects.all()
    return render(request, 'autoDeploy.html', locals())

def get_pkgs(request):
    config_info = ConfigTable.objects.all()
    sections = ConfigTable.objects.filter(section_flag=1).exclude(section='public')
    # 获取token数据
    light_token_data = ConfigTable.objects.get(section='public', option='light', section_flag=0)
    pkg_token_data = ConfigTable.objects.get(section='public', option='pkg', section_flag=0)
    light_token = json.loads(light_token_data.value)
    pkg_token = json.loads(pkg_token_data.value)
    light_date_time = light_token_data.date_time
    pkg_date_time = pkg_token_data.date_time
    return render(request, 'light.html', locals())
    # return HttpResponse('light.html')

@csrf_exempt    
def deploy_on_lihgt(request):
    # Get the value of argues
    section = request.POST['section']
    light_token = request.POST['light_token'].strip()
    pkg_token = request.POST['pkg_token'].strip()
    file = request.FILES['file']
    path = request.POST['path']
    
    # if both file and path is existed, use file, drop path.
    if file:
    # deal with upload file.
        try:
            file_path = os.path.join(settings.UPLOAD_FILE_ROOT, file.name)
            with open(file_path, 'wb') as f:
                for info in file.chunks():
                    f.write(info)
            print('Upload File Successfully.')
        except Exception as e:
            print(str(e))
            return HttpResponse('Upload File Failed.')
    else:
        if pkg_token:
            pkg_token = {"Cookie": pkg_token}
        else:
            pkg_token = json.loads(ConfigTable.objects.get(section='public', option='pkg', section_flag=0).value)
        download = Download(file_path=path, headers=pkg_token)
        download.download(settings.DOWNLOAD_FILE_PATH)
        if os.path.getsize(os.path.join(settings.DOWNLOAD_FILE_PATH, os.path.basename(path))) < 1000:
            return HttpResponse('PKG Token May Be Overdue. Please Reset It.')
    
    # IF light_token was not given, then got it from table.
    if light_token:
        light_token = {"Authorization": light_token}
    else:
        light_token = json.loads(ConfigTable.objects.get(section='public', option='light', section_flag=0).value)

    # ids = {app_id: pkg_id}
    ids = json.loads(ConfigTable.objects.get(section=section, option="ids", section_flag=0).value)
    deploy = DeployOnLight(headers=light_token)
    for app_id, pkg_id in ids.items():
        try:
            deploy.deploy(file_path=os.path.join(settings.UPLOAD_FILE_ROOT, file.name),
            app_id=app_id, pkg_id=pkg_id)
        except Exception as e:
            print(str(e))
            return HttpResponse('The Light Token is probably overdue.')
        
    # return render(request, 'light.html', locals())
    return HttpResponse('Deploy {0} on app {1} Successfully.'.format(file.name, section))