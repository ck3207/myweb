from django.db import models

# Create your models here.


class Tool(models.Model):
    """标签表"""
    name = models.CharField(max_length=32, verbose_name="工具名")
    description = models.CharField(max_length=512, verbose_name="描述")
    detail = models.CharField(max_length=32, verbose_name="详情")

    def __str__(self):
        return self.name
