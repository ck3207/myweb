from django.shortcuts import render
from .models import LableNum, LableDetail
# Create your views here.

def homepage(request):
    all_tables = LableNum.objects.all()
    tables_num = len(all_tables)
    return render(request, 'home.html', locals())


def get_labels(request):
    all_tables = LableNum.objects.all()
    tables_num = len(all_tables)
    return render(request, 'lable.html', locals())


def get_lable_detail(request, lable_name='acct_wt_user_fund_income_value'):
    detail = LableDetail.objects.filter(table_name=lable_name)
    return render(request, 'lable_detail.html', locals())


def get_detail(request, table_name="acct_wt_user_money_in_out"):
    detail = LableDetail.objects.filter(table_name=table_name).order_by("column_name", "interval_type")
    label_num = LableNum.objects.get(table_name=table_name)

    return render(request, 'detail.html', locals())