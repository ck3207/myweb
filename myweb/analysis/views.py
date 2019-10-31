from django.shortcuts import render
import os
import django
os.environ.update({"DJANGO_SETTINGS_MODULE": "myweb.settings"})
django.setup()
from models import LableNum, LableDetail
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
    detail = LableDetail.objects.get(lable_name)
    return render(request, 'lable_detail.html', {'detail': detail})

