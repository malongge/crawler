#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import unicodecsv as csv
import re
from PIL import Image
import pytesseract
import cv2 as cv
from skimage import io

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
    url = "http://47.52.164.88/test8.php?id="+str(id)
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
    
    return course_all_num


def get_and_save_price_pic(id):
    image_url = "http://47.52.164.88/price.png"
    save_pic_name = "price"+str(id)+".png"
    try:
        r = requests.get(image_url,proxies=proxies,headers=headers)
        result = r.content
        with open(save_pic_name,'wb') as f:
            f.write(result)
    except requests.exceptions.RequestException as e:
        print(e)
    return save_pic_name    

def parse_picture(save_pic_name):
    image = cv.imread(save_pic_name)
    text = pytesseract.image_to_string(Image.fromarray(image))
    print u"解析图片中...."
    print u"解析的结果是：",text
    return text


def main():
    for i in range(1,21):
        response = get_pages(i)
        classnum = parse_response(response)
        save_pic_name = get_and_save_price_pic(i)
        price = parse_picture(save_pic_name)
        print u"爬取结果："
        print u'课程id:',str(i),u' 课程数目: ',classnum,u'课程价格: ',price

if __name__ == "__main__":
    main()