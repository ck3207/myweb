from django.db import models
# Create your models here.


class LableNum(models.Model):
    """Load Data From Pickle File."""
    table_name = models.CharField(max_length=128, primary_key=True)
    table_num = models.IntegerField()

    def __unicode__(self):
        return self.table_name


class LableDetail(models.Model):
    """Load Data From Pickle File."""
    table_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=128, default='')
    column_name = models.CharField(max_length=64, default='')
    fund_account_max = models.CharField(max_length=16, default='')
    fund_account_min = models.CharField(max_length=16, default='')
    interval_type = models.CharField(max_length=4, default='')
    max_value = models.CharField(max_length=512, default='')
    min_value = models.CharField(max_length=512, default='')
    null_value = models.CharField(max_length=512, default='')

    def __unicode__(self):
        return self.table_name


class Tools(models.Model):
    """测试工具数据库"""
    name = models.CharField(max_length=16, default='')
    summary = models.CharField(max_length=512, default='')
    url = models.CharField(max_length=64, default='')

    def __unicode__(self):
        return self.name


class Servers(models.Model):
    """服务器信息数据库"""
    id = models.IntegerField(primary_key=True, auto_created=True)
    address = models.CharField(max_length=16, default='')
    port = models.IntegerField()
    user = models.CharField(max_length=32, default='')
    password = models.CharField(max_length=64, default='')


    class Meta:
        unique_together = ('address', 'port', 'user')