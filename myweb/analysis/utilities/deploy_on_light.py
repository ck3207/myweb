# -*- coding: utf-8 -*-
import time
import os
import zipfile
import requests
import sys
import json
import logging

import configparser
# from download_flies_from_ftp import FtpOperate
# from download_files_from_pkg import PKG

__author__ = "chenk"


class DeployOnLight:
    """Deploy on light."""
    BASE_URL = "https://fs-api.lightyy.com/"
    COMPONENTS = {"form-restrict": 523,
            "large-transaction": 528,
            "margin-trading": 529,
            "national-team": 532,
            "performance-announcement": 524,
            "share-dividend": 526,
            "share-pledge": 527,
            "stock-diagnosticate": 531,
            "fund-flow": 545,
            "stop-and-return": 578,
            "accountanalysis-cnpsec": 604,
            "h5-fans-cnpsec": 644,
            "fans": 760
            }

    def __init__(self, headers):
        self.headers = headers

    def query_offline_pkglist(self, url="service/portal/appdiy/offline/query_offline_pkglist", data={"app_id": "2968"}):
        """Response column:
        pkg_id: pkg_id
        name: pkg name"""
        return self.request(url=DeployOnLight.BASE_URL+url, data=data, is_get=True)

    def query_offline_pkglist2(self, url="service/portal/appdiy/offline/query_offline_pkglist"):
        data = {"app_id": "2968"}
        r = requests.get(url=DeployOnLight.BASE_URL + url, headers=self.headers, verify=False, params=data)
        logging.info(r.json())

    def query_offline_versionlist(self, data, url="service/portal/appdiy/offline/query_offline_versionlist"):
        """Response column:
        status:0 待发布
        status:1 发布中
        status:2 已结束"""
        return self.request(url=DeployOnLight.BASE_URL + url, data=data, is_get=True)

    def get_current_version_info(self, data={}):
        version = {}
        result = data
        try:
            for version in result.get("data").get("list"):
                if version.get("status") == "1":
                    return version
        except Exception as e:
            logging.error("Error: {0}".format(str(e)))
        finally:
            return version

    def get_max_version_info(self, data={}):
        version = {}
        result = data
        try:
            for version in result.get("data").get("list"):
                return version
        except Exception as e:
            logging.error("Error: {0}".format(str(e)))
        finally:
            return version

    def upload_package(self, file_path, url="file/light/package"):
        """Response column:
        pkg_id: pkg_id
        name: pkg name"""
        files = {"file": open(file_path, "rb")}
        result = requests.post(url=DeployOnLight.BASE_URL+url, files=files, headers=self.headers, verify=False)
        logging.info(result.json())
        return result.json()

    def add_offline_version(self, url="service/portal/appdiy/offline/add_offline_version", data={}):
        """Response column:
        new_version_id: id"""
        return self.request(url=DeployOnLight.BASE_URL+url, data=data, is_get=False)

    def query_offline_task(self, url="service/portal/appdiy/offline/query_offline_task", data={}):
        """Response column:
        task_id: id"""
        return self.request(url=DeployOnLight.BASE_URL+url, data=data, is_get=True)

    def update_offline_task(self, url="service/portal/appdiy/offline/update_offline_task", data={}):
        """Response column:
        """
        return self.request(url=DeployOnLight.BASE_URL+url, data=data, is_get=False)

    def add_offline_task(self, url="service/portal/appdiy/offline/add_offline_task", data={}):
        """Response column:
        task_id
        """
        return self.request(url=DeployOnLight.BASE_URL+url, data=data, is_get=False)

    def request(self, url, data, is_get=True, verify=False, headers={}):
        logging.info("Will Reuqeuest Interface: {0}".format(url))
        logging.info("Augues as follows: \n{0}".format(data))
        if not headers:
            headers = self.headers
        if is_get:
            r = requests.get(url=url, headers=headers, verify=verify, params=data)
        else:
            r = requests.post(url=url, headers=headers, verify=verify, data=data)
        result = r.json()
        logging.info("Response: \n{0}".format(result))
        return result

    def get_next_version(self, current_version):
        """Get next version. Example, old version is 1.0.2,
        then next version is 1.0.3."""
        current_version_list = current_version.split(".")
        next_value = str(int(current_version_list.pop()) + 1)
        current_version_list.append(next_value)
        return ".".join(current_version_list)

    def get_package_id(self, file_name):
        """Every package has its own package_id. It generated when it was added. 
        These id can be found on light platform."""
        for key in DeployOnLight.COMPONENTS.keys():
            if key in file_name:
                return DeployOnLight.COMPONENTS.get(key)

    def get_task_id(self, data={}):
        """Get the task_id which is deployed now."""
        try:
            for task in data.get("data").get("list"):
                if task.get("status") == '0' or task.get("status") == 0:
                    return task.get("id")
        except Exception as e:
            logging.error(str(e))

    def deploy(self, file_path, app_id, pkg_id):
        pkg_list = self.query_offline_pkglist(data={"app_id": app_id})
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        time.sleep(0.5)

        # 判断 app　是否在部署app列表中
        for component in pkg_list.get("data"):
            # 下述处理逻辑必需为 匹配ID后，进行更新操作，即使代码有问题， 也不会影响其他组件，切记！切记！
            if component.get("id") == int(pkg_id):
                name = component.get("name")
                pkg_id = component.get("id")
                logging.info("H5[{0}], pkg_id [{1}], pkg_id_type [{2}]".format(name, pkg_id, type(pkg_id)))
                continue
                data = {"app_id": app_id, "pkg_id": pkg_id, "page_no": 1, "page_size": 10}
                deployed_version_dic = self.query_offline_versionlist(data=data)
                upload_data_dic = self.upload_package(file_path=file_path)
                deployed_version_info = self.get_current_version_info(data=deployed_version_dic)
                deployed_version_id = deployed_version_info.get("id")
                max_version = self.get_max_version_info(data=deployed_version_dic).get("version")
                new_version = self.get_next_version(current_version=max_version)
                android_version_scope = ios_version_scope = "0.0.0.0,9.9.9.9"
                package_id = upload_data_dic.get("data")
                add_offline_version_data = {"app_id": app_id, "pkg_id": pkg_id, "version": new_version,
                                            "android_version_scope": android_version_scope,
                                            "ios_version_scope": ios_version_scope, "is_wifi": 0,
                                            "package_id": package_id, "file_name": file_name, "file_size": file_size}
                offline_version_dic = self.add_offline_version(data=add_offline_version_data)
                query_offline_task_data = {"app_id": app_id, "version_id": deployed_version_id, "page_no": 1, "page_size": 5}
                query_offline_task_dic = self.query_offline_task(data=query_offline_task_data)
                task_id = self.get_task_id(query_offline_task_dic)
                update_offline_task_data = {"app_id": app_id, "id": task_id, "status": 2}
                self.update_offline_task(data=update_offline_task_data)
                new_version_id = offline_version_dic.get("data")
                add_offline_task_data = {"app_id": app_id, "pkg_id": pkg_id, "version_id": new_version_id,
                                         "release_type": 0, "update_strategy": 0, "release_desc": "Auto Deployed."}
                self.add_offline_task(data=add_offline_task_data)
        return
