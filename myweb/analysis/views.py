from django.shortcuts import render
from .models import LableNum, LableDetail
# Create your views here.

def homepage(request):
    return render(request, 'home.html')


def get_labels(request):
    lables = []
    for i in range(10):
        lable = "标签" + str(i)
        lables.append(lable)
    return render(request, 'lable.html', {'lables': lables})


def get_lable_detail(request, lable_name='acct_wt_user_fund_income_value'):
    detail = LableDetail.objects.filter(table_name=lable_name)
    return render(request, 'lable_detail.html', locals())


def get_detail(request):
    table_name = "acct_wt_user_fund_income_value"
    details = []
    detail = LableDetail.objects.filter(table_name=table_name).order_by("column_name", "interval_type")
    label_num = LableNum.objects.filter(table_name=table_name)

    return render(request, 'detail.html', locals())