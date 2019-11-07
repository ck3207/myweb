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
    table_name = models.CharField(max_length=128)
    column_name = models.CharField(max_length=64, default='')
    fund_account = models.CharField(max_length=16)
    interval_type = models.CharField(max_length=4)
    max_value = models.CharField(max_length=512)
    min_value = models.CharField(max_length=512)
    null_value = models.CharField(max_length=512)

    def __unicode__(self):
        return self.table_name

