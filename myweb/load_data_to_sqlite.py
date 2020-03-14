# -*- coding: utf-8 -*-
import pickle
import os
import django
os.environ.update({"DJANGO_SETTINGS_MODULE": "myweb.settings"})
django.setup()

from analysis.models import LableNum, LableDetail
from analysis.models import Tools
__author__ = "chenk"


def load_data_to_sqlite_of_labels(file_name="data.pkl"):
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


def load_data_to_sqlite_of_tools():
    tools = {"标签数据统计": ["可查阅所有统计标签，列出标签的一些基本信息；\
    比如 某一计算日的标签总数量，标签每个维度的极值，标签每个维度的空值情况；", "/labels"],
             "正交表转化": ["通过正交表查询网站(http://support.sas.com/techsup/technote/ts723_Designs.txt)，\
              找到符合的正交表，然后设置正交表的有效列，以及实际填充值，\
              最终生成一个可直接复制到excel的正交表；", "/orthogonalArray"],
             "添加Linux远程服务器": ["添加远程服务器，以备其他远程连接使用；\
             比如：自动化部署，需要连接远程服务器；", "/addHost"],
             "上传文件": ["可上传文件到服务器", "/uploadFile"],
             "自动化部署": ["通过执行服务器上的命令，来实现远程部署", "/autoDeploy"]}
    Tools.objects.all().delete()
    for name, values in tools.items():
        Tools.objects.create(name=name, summary=values[0], url=values[1])

    return


if __name__ == "__main__":
    # os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})
    # load_data_to_sqlite_of_labels()
    load_data_to_sqlite_of_tools()
