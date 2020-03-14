from django.shortcuts import render
from .models import LableNum, LableDetail, Tools, Servers
from .orthogonalArray.config import Config
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


def get_orthogonal_array_info(request):
    config = Config(config_file="conf/conf.ini")
    factor, col, split = config.get_config()
    col = ",".join(col)
    return render(request, 'orthogonal_array.html', locals())


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
        # return render(request, 'result.html', locals())
        return HttpResponse("Insert data successfully.")
    except Exception as e:
        return HttpResponse('Insert data failured.Probably data have already existed.')

def del_data(request):
    db_info = {'servers': Servers}
    db_name = request.GET['db_name']
    db_info.get(db_name).objects.all().delete()
    return HttpResponse('Del Data Successfully.')


def autoDeploy(request):
    datas = Servers.objects.all()
    return render(request, 'autoDeploy.html', locals())

