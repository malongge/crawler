#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import unicodecsv as csv
import re


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
    url = "http://47.52.164.88/test7.php?id="+str(id)
    try:
        # print 'crawlling: '+str(id)
        r = requests.get(url, proxies=proxies,headers=headers)
        # r = requests.get(url,headers=headers)
        result = r.content.decode('utf-8')
    except requests.exceptions.RequestException as e:
        print(e)
        print('retring'+str(id))
    return result

def parse_response(response):
    soup = BeautifulSoup(response,'lxml')
    #get course numbers
    course_all_num_string = soup.find('span',class_="test").string
    #get the exact value from the whole string
    course_all_num = str(re.findall(r'\d+',course_all_num_string)[0])
    course_all_num = convert_num(course_all_num)
    #1.get the span by class name:discount-price
    #2.get the second span
    price = soup.find_all('span',class_='test')[1].string
    price = convert_num(price)
    
    return course_all_num,price


def convert_num(num):
    '''
    convert numbers:1->2,2->4,3->1,4->5,5->3,6->7,7->6,
    '''
    tmp_string = str(num)
    new_num_string = ''
    for digit in tmp_string:
        new_num_string += str(convert_digit(digit))
    return int(new_num_string)

def convert_digit(digit):
    digit = int(digit)
    if digit == 1:
        result = 2
        pass
    elif digit == 2:
        result = 4
        pass
    elif digit == 3:
        result = 1
        pass
    elif digit == 4:
        result = 5
        pass
    elif digit == 5:
        result = 3
        pass
    elif digit == 6:
        result = 7
        pass
    elif digit == 7:
        result =6
    elif digit ==8:
        result =8
        pass
    elif digit == 9:
        result = 9
        pass
    elif digit == 0:
        result = 0
    
    return result



def main():
    for i in range(1,18):
        response = get_pages(i)
        classnum,price = parse_response(response)
        print('id:',str(i),' classnum: ',classnum,' price: ',price)

if __name__ == "__main__":
    main()