#!/usr/bin/python
#coding:utf-8

import requests
import unicodecsv as csv
import re
import json

queuenum = 50
save_file_name = "result_all_3_multithreading-200-1.csv"
proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080",
}

headers = {
    "Host": "47.52.164.88",
    "Origin": "http://47.52.164.88",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://www.baidu.com",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "close"
}

def get_pages(id):
    url = "http://47.52.164.88/test3.php?id="+str(id)
    try:
        print 'crawlling: '+str(id)
        r = requests.get(url, proxies=proxies,headers=headers)
        # r = requests.get(url,headers=headers)
        result = r.content.strip()
    except requests.exceptions.RequestException as e:
        print(e)
        print('retring'+str(i))
    return result

def parse_response(response):
    data = json.loads(response)
    classnum = data['classnum']
    price = data['price']
    return classnum,price

def main():
    for i in range(1,21):
        response = get_pages(i)
        classnum,price = parse_response(response)
        print('id:',str(i),' classnum: ',classnum,' price: ',price)

if __name__ == "__main__":
    main()