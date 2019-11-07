# -*- coding: utf-8 -*-
import pickle
import os
import django
os.environ.update({"DJANGO_SETTINGS_MODULE": "myweb.settings"})
django.setup()

from analysis.models import LableNum, LableDetail
__author__ = "chenk"


def load_data_to_sqlite(file_name="data.pkl"):
    """从文件中导入数据，文件存储数据格式为：
    "table_name"：
    {'income_value': 
        {'null': [], 
        'min': [['19880822', '-397173.094', '1'], 
                ['19880822', '-1279515.716', '2'], 
                ['19917735', '-5339580.064', '3'], 
                ['19917735', '-5063959.25', '4']], 
        'max': [['95147149', '5028430.43', '1'], 
                ['95147149', '5029277.47', '2'], 
                ['95147149', '20046562.31', '3'], 
                ['95147149', '20051023.71', '4']]}, 
    'num': 648590, 
    'asset_prop': 
        {'null': [], 
        'min': [['10001130', '0', '1'], 
                ['10000763', '0', '2'], 
                ['10001939', '0', '3'], 
                ['10000496', '0', '4']], 
        'max': [['920108491', '7', '1'], 
                ['919882338', '7', '2'], 
                ['919885483', '7', '3'], 
                ['910021223', '7', '4']]}}
    """
    with open(file=file_name, mode="rb") as f:
        data = pickle.load(f)

    LableNum.objects.all().delete()
    LableDetail.objects.all().delete()
    for table_name, info in data.items():
        LableNum.objects.create(table_name=table_name, table_num=info.get("num"))
        for column, column_info in info.items():
            if not column == "num":
                # value_type=0, null值; value_type=1, 最小值; value_type=2,最大值
                for value_type in [0, 1, 2]:
                    if value_type == 0:
                        value_type_d = "null"
                    elif value_type == 1:
                        value_type_d = "min"
                    else:
                        value_type_d = "max"
                    for each in column_info.get(value_type_d):
                        if len(each) > 0:
                            fund_account = each[0]
                            value = each[1]
                            interval_type = each[2]
                            LableDetail.objects.create(table_name=table_name,
                                                       column_name=column,
                                                       fund_account=fund_account,
                                                       value=value,
                                                       value_type=value_type,
                                                       interval_type=interval_type)
                            print(table_name, column, value_type, interval_type, value)
                # 当没有最大值、最小值、NULL值的数据时，插入一条数据缺失的数据
                for tmp in range(3):
                    l = LableDetail.objects.filter(table_name=table_name,
                                               column_name=column,
                                               value_type=tmp)
                    try:
                        l[0]
                    except Exception:
                        LableDetail.objects.create(table_name=table_name,
                                                   column_name=column,
                                                   fund_account='--',
                                                   value='--',
                                                   value_type=tmp,
                                                   interval_type="--")
                        print(table_name, column, tmp, "--", "--")


if __name__ == "__main__":
    # os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})
    load_data_to_sqlite()
