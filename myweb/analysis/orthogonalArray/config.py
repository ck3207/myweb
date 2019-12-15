# -*- coding: utf-8 -*-
import configparser
import json
__author__ = "chenk"

class Config:
    def __init__(self, config_file=".conf/conf.ini"):
        self.config_file = config_file
        self.cf = configparser.ConfigParser()

    def get_config(self):
        """获取配置项信息"""
        import os
        if os.path.exists(self.config_file):
            self.cf.read(filenames=self.config_file, encoding="utf-8")
            factor = json.loads(self.cf.get(section="section", option="factor"))
            col = self.cf.get(section="section", option="col").split(",")
            split = self.cf.get(section="section", option="split").strip()
        else:
            factor, col, split = {}, [], os.path.join(os.getcwd(), self.config_file)
        return factor, col, split

    def set_config(self, factor, col):
        if not factor:
            return "Factor can't be null."
        elif not col:
            return "Col can't be null."
        self.cf.add_section("section")
        self.cf.set("section", "factor", factor)
        self.cf.set("section", "col", col)


if __name__ == "__main__":
    print(Config().get_config())