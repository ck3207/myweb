import json

import configparser


class ConfigInfo:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(filenames="conf-pkgs.ini", encoding="utf-8")
        
    def get_tokens(self):
        try:
            light_header = json.loads(self.cf.get(section="public", option="light"))
        except Exception as e:
            pass
        return light_header
        
    def set_tokens(self, name, token, section='public'):
        self.cf.set(section, name, token)
    
    def get_infos(self, section='zhongyou-fans'):
        # light_header = self.get_tokens()
        # pkg_header = json.loads(cf.get(section="public", option="pkg"))
        # light_header = json.loads(cf.get(section="public", option="light"))
        update_packages = self.cf.get(section=section, option="update_packages").strip()
        ids = json.loads(self.cf.get(section=section, option="ids"))
        return update_packages, ids
        
    def sections(self):
        return self.cf.sections()
        
    def cf_object(self):
        return self.cf
        
if __name__ == "__main__":
    config_info = ConfigInfo()
    cf = config_info.cf_object()
    Config.objects.all().delete()
    for section in cf.sections():
        for option in cf.options(section):
            print(section, option, cf.get(section=section, option=option))
            Config.objects.create(section=section, option=option, value=cf.get(section=section, option=option))