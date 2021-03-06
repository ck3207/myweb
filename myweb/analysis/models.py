from django.db import models
import django.utils.timezone as timezone

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


class Urls(models.Model):
    """测试工具数据库"""
    id = models.IntegerField(default='', verbose_name="url的id", primary_key=True)
    name = models.CharField(max_length=16, default='', verbose_name="url的名字")
    summary = models.CharField(max_length=512, default='', verbose_name="url的功能简介")
    url = models.CharField(max_length=64, default='', verbose_name="url地址")
    parent_url_id = models.IntegerField(default=0, verbose_name="上一级url的id")

    def __unicode__(self):
        return self.name

    class Meta:
        # 表备注
        verbose_name = "url信息表"

class FileTransfer(models.Model):
    """测试工具数据库"""
    # id = models.IntegerField(default='', verbose_name="url的id", primary_key=True)
    name = models.CharField(max_length=256, default='', verbose_name="文件的URL")
    type = models.IntegerField(default=0, verbose_name="1:上传， 2:下载")
    remark = models.CharField(max_length=512, default='', verbose_name="备注")
    create_time = models.DateTimeField(default=timezone.now, auto_created=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.name

    class Meta:
        # 表备注
        verbose_name = "文件传输表"

class Servers(models.Model):
    """服务器信息数据库"""
    id = models.IntegerField(primary_key=True, auto_created=True)
    address = models.CharField(max_length=16, default='')
    port = models.IntegerField()
    user = models.CharField(max_length=32, default='')
    password = models.CharField(max_length=64, default='')


    class Meta:
        unique_together = ('address', 'port', 'user')
        
        
class ConfigTable(models.Model):
    """配置表
    当 section_flag 字段为 1时， 此数据为 section 数据；
    当 section_flag 字段为 0时， 此数据为 section 下各个option 的数据；
    """
    id = models.IntegerField(primary_key=True, auto_created=True)
    section = models.CharField(max_length=32, default='')
    option = models.CharField(max_length=32, default='')
    value = models.CharField(max_length=512, default='')
    section_flag = models.BooleanField(default=0)
    version = models.CharField(max_length=128, default='')
    date_time = models.DateTimeField(auto_now=True)
    
    
class SmallTools(models.Model):
    """ 小组件表，记录小组件部署服务器、以及部署路径，升级脚本等信息 """
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=32, default='')
    host = models.CharField(max_length=32, default='')
    script = models.CharField(max_length=32, default='')
    command = models.CharField(max_length=256, default='')
    

