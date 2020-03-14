# -*- coding: utf-8 -*-
__author__ = "chenk"

import paramiko


class Connect:
    """此类可通过SSH连接远程服务器"""
    def __init__(self):
        pass

    def connect(self, host, port, user, password):
        # 实例化对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 建立连接
        ssh.connect(hostname=host, port=port, username=user, password=password)
        return ssh

    def executeComand(self, command):
        pass
        # ssh._transport = trans
        # # 执行命令，和传统方法一样
        # stdin, stdout, stderr = ssh.exec_command('df -hl')
        # print(stdout.read().decode())
        #
        # # 关闭连接
        # trans.close()


if __name__ == "__main__":
    c = Connect()
    ssh = c.connect(host="10.20.18.174", port=22, user="root", password="Hsidc@78")
    stdin, stdout, stderr = ssh.exec_command("pwd")
    print(stdin, stdout.read(), stderr)