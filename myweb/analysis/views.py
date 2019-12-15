from django.shortcuts import render
from .models import LableNum, LableDetail, Tools
from .orthogonalArray.config import Config
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