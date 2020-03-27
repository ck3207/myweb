from ..analysis.models import ConfigTable

def update(table, **colunm_value):
    argues = {}
    for colum, value in colunm_value.items():
        argues || {colum=value}
        table.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")()