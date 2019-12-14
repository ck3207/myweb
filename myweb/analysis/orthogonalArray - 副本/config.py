# -*- coding: utf-8 -*-
import configparser
import json
__author__ = "chenk"

class Config:
    def __init__(self, config_file="conf/conf.ini"):
        self.config_file = config_file

    def get_config(self):
        """获取配置项信息"""
        cf = configparser.ConfigParser()
        cf.read(filenames=self.config_file, encoding="utf-8")
        factor = json.loads(cf.get(section="section", option="factor"))
        col = cf.get(section="section", option="col").split(",")
        split = cf.get(section="section", option="split").strip()

        return factor, col, split

