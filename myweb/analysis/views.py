import json
import os

from django.shortcuts import render, redirect
from django.conf import settings
from .models import LableNum, LableDetail, Tools, Servers, ConfigTable
# from .orthogonalArray.config import Config as c
from .conf.config import ConfigInfo
from .utilities.deploy_on_light import DeployOnLight
from .utilities.download_from_pkg import Download
from .utilities.replace_config_file import Replace
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
import logging


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
    light_token = json.loads(light_token_data.value.replace("'", '"'))
    pkg_token = json.loads(pkg_token_data.value.replace("'", '"'))
    light_date_time = light_token_data.date_time
    pkg_date_time = pkg_token_data.date_time
    return render(request, 'light.html', locals())


@csrf_exempt    
def deploy_on_lihgt(request):
    # Get the value of argues
    section = request.POST['section']
    light_token = request.POST['light_token'].strip()
    pkg_token = request.POST['pkg_token'].strip()
    file = request.FILES['file']    # 上传的文件
    pkg_full_path = request.POST['path'] # 需要下载的pkg文件全路径
    logging.info('Input pkg_token: {0}'.format(pkg_token))
    logging.info('Input light_token:{0}'.format(light_token))
    # 获取部署包
    # if both file and path is existed, use file, drop path.
    if file:
    # deal with upload file.
        try:
            file_full_path = os.path.join(settings.UPLOAD_OR_DOWNLOAD_FILE_PATH, file.name)
            with open(file_full_path, 'wb') as f:
                for info in file.chunks(chunk_size=1024):
                    f.write(info)
            logging.info('Upload File[{0}] Successfully.'.format(file_full_path))
        except Exception as e:
            logging.info(str(e))
            logging.info('Upload File[{0}] Failed.'.format(file_full_path))
            return HttpResponse('Upload File Failed.')
    else:
        file_full_path = os.path.join(settings.UPLOAD_OR_DOWNLOAD_FILE_PATH, os.path.basename(pkg_full_path))
        if pkg_token:
            pkg_token = {"Cookie": pkg_token}
        else:
            pkg_token = json.loads(ConfigTable.objects.get(section='public', option='pkg', section_flag=0).value)
            logging.info('Get pkg_token from ConfigTable is [{}]'.format(pkg_token))
        # 下载部署包
        download = Download(file_path=pkg_full_path, headers=pkg_token)
        download.download(settings.UPLOAD_OR_DOWNLOAD_FILE_PATH)
        # whether the target file is downloaded or not via the size of download file.
        if os.path.getsize(file_full_path) < 1000:
            return HttpResponse('PKG Token May Be Overdue. Please Reset It.')
        else:
            # update pkg token
            logging.info("Download file[{0}] successfully.".format(pkg_full_path))
            ConfigTable.obejects.filter(section='public', option='pkg', section_flag=0).update(value=pkg_token)
            logging.info('Update pkg token[{0}].'.format(pkg_token))
            # logging.info(str(pkg_token))
    
    # 解压部署包，替换配置文件， 压缩部署包
    try:
        logging.info("Trying to replace config file.")
        rep = Replace(file_path=file_full_path, section=section)
        # src_dir=压缩源目录， dest_dir=压缩到哪个目录， file_name=压缩后的文件名
        logging.debug('Trying to unzip download zip file[{0}].'.format(file_full_path))
        src_dir, dest_dir, file_name = rep.unzip_file()
        logging.debug("src_dir is {0}, dest_dir is {1}, file_name is {2}".format(src_dir, dest_dir, file_name))
        logging.info("Trying to replace config file.")
        rep.replace_config(os.path.join(settings.UPLOAD_OR_DOWNLOAD_FILE_PATH, section), src_dir, "config.local.js")
        logging.info("Trying to zip the directory after replacing config file.")
        new_file_full_path = rep.zip_file(src_dir=src_dir, dest_dir=dest_dir, file_name=file_name)
        logging.info('Replaced config file successfully.')
    except:
        logging.info(('Unzip or Zip file error: {0}'.format(os.path.basename(file_full_path))))
        return HttpResponse('Unzip or Zip file error: {0}'.format(os.path.basename(file_full_path)))

    # light 部署
    # IF light_token was not given, then got it from table.
    if light_token:
        light_token = {"Authorization": light_token}
    else:
        light_token = json.loads(ConfigTable.objects.get(section='public', option='light', section_flag=0).value)
        logging.info('Get light_token from ConfigTable is [{}]'.format(light_token))
    # ids = {app_id: pkg_id}
    ids = json.loads(ConfigTable.objects.get(section=section, option="ids", section_flag=0).value)
    logging.info("需要部署的APP 信息: {}".format(ids))
    deploy = DeployOnLight(headers=light_token)
    for app_id, pkg_id in ids.items():
        try:
            deploy.deploy(file_path=new_file_full_path, app_id=app_id, pkg_id=pkg_id)
            # update light token
            ConfigTable.objects.filter(section='public', option='light', section_flag=0).update(value=light_token)
            logging.info('Update light token[{0}].'.format(light_token))
            # logging.info(str(light_token))
        except Exception as e:
            logging.info(str(e))
            logging.info('The Light Token is probably overdue.')
            return HttpResponse('The Light Token is probably overdue.')
        
    logging.info('Deploy {0} on app {1} Successfully.'.format(file.name, section))
    return HttpResponse('Deploy {0} on app {1} Successfully.'.format(file.name, section))