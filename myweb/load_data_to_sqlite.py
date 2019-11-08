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
                # 初始化字段值
                fund_account_max, fund_account_min, interval_type = "--", "--", "--"
                max_value, min_value, null_value = "--", "--", "--"

                max_values = column_info.get("max")
                min_values = column_info.get("min")

                # 同一字段 如果有最大值，那么就有最小值，但是有可能不是每个interval_type都有数据
                for i in range(len(max_values)):
                    # 初始化字段值
                    fund_account_max, fund_account_min, interval_type = "--", "--", "--"
                    max_value, min_value, null_value = "--", "--", "--"
                    if max_values[i][2] < min_values[i][2]:
                        interval_type = max_values[i][2]
                        fund_account_max = max_values[i][0]
                        max_value = max_values[i][1]
                    elif max_values[i][2] > min_values[i][2]:
                        interval_type = min_values[i][2]
                        fund_account_min = min_values[i][0]
                        min_value = min_values[i][1]
                    else:
                        fund_account_max = max_values[i][0]
                        max_value = max_values[i][1]
                        fund_account_min = min_values[i][0]
                        min_value = min_values[i][1]
                        interval_type = max_values[i][2]
                    null_values = column_info.get("null", '')
                    try:
                        null_value = null_values[i]
                    except IndexError:
                        pass
                    #  插入数据
                    LableDetail.objects.create(table_name=table_name,
                                               column_name=column,
                                               interval_type=interval_type,
                                               fund_account_max=fund_account_max,
                                               max_value=max_value,
                                               fund_account_min=fund_account_min,
                                               min_value=min_value,
                                               null_value=null_value)
                    print(table_name, column, interval_type, max_value, min_value, null_value)


if __name__ == "__main__":
    # os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})
    load_data_to_sqlite()
