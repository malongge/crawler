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
    url = "http://47.52.164.88/test6.php?id="+str(id)
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
    course_all_num_string = soup.find('span',class_="course-all-num").string
    #get the exact value from the whole string
    course_all_num = str(re.findall(r'\d+',course_all_num_string)[0])
    #1.get the span by class name:discount-price
    #2.get the second span
    price_span = soup.find('span',class_='discount-price').find_all('span')[1]
    color_fff_num = count_color_fff(price_span)
    
    price_value = 0
    #judge by color_fff_num, which case it is. 2 digits, 3 digits or 4 digits, and 
    if color_fff_num == 3:
        price_value = parse_price_2_digits(price_span)
    elif color_fff_num == 1:
        price_value = parse_price_3_digits(price_span)
    elif color_fff_num == 0:
        price_value = parse_price_4_digits(price_span)
    return course_all_num,price_value


def count_color_fff(price_span):
    '''
    count the number of <i> contains "color:#fff"
    '''
    i_count = 0
    for i_tag in price_span.find_all('i'):
        if "color:#fff" in i_tag['style']:
            # print i_tag['style']
            i_count += 1
    return i_count



def parse_price_2_digits(price_span):
    price_string = ''
    price_string = price_span.find_all('i')[0].string
    price_string += price_span.find_all('i')[5].string
    return price_string

def parse_price_3_digits(price_span):
    price_string = ''
    price_string = price_span.find_all('i')[0].string
    price_string += price_span.find_all('i')[1].string
    price_string += price_span.find_all('i')[4].string
    return price_string

def parse_price_4_digits(price_span):
    price_string = ''
    price_string = price_span.find_all('i')[0].string
    price_string += price_span.find_all('i')[5].string
    price_string += price_span.find_all('i')[4].string
    price_string += price_span.find_all('i')[3].string
    return price_string


def main():
    #演示时，就使用range(101,128),会包含3种不同长度的数字
    for i in range(101,128):
        response = get_pages(i)
        classnum,price = parse_response(response)
        print('id:',str(i),' classnum: ',classnum,' price: ',price)

if __name__ == "__main__":
    main()