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

proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080",
}
save_file_name = "result_all_2.csv"

headers = {
    "Host": "47.52.164.88",
    "Origin": "http://47.52.164.88",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://47.52.164.88/",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "close"
}

def get_pages(s,id):
    url = "http://47.52.164.88/test2.php?id="+str(id)
    try:
        r = s.get(url, proxies=proxies,headers=headers,allow_redirects=False)
        # r = requests.get(url,headers=headers)
        html_content = r.content.decode('utf-8')
        get_status_code = r.status_code
    except requests.exceptions.RequestException as e:
        print(e)
        print('retring'+str(id))
    return get_status_code,html_content


def get_and_save_captcha_pic(s,id):
    image_url = "http://47.52.164.88/image.php"
    save_pic_name = "captcha"+str(id)+".png"
    try:
        r = s.get(image_url,proxies=proxies,headers=headers)
        result = r.content
        with open(save_pic_name,'wb') as f:
            f.write(result)
    except requests.exceptions.RequestException as e:
        print(e)
    return save_pic_name

def parse_captcha_pic(save_pic_name):
    image = cv.imread(save_pic_name)
    text = pytesseract.image_to_string(Image.fromarray(image))
    return text

def post_captcha(s,captcha_text):
    post_url = "http://47.52.164.88/post2.php"
    post_data = {'code':captcha_text,'Submit':'%E7%99%BB%E5%BD%95'}
    r = s.post(post_url,proxies=proxies,data=post_data,allow_redirects=False)
    verified = False
    if u"验证码正确" in r.content.decode('utf-8'):
        verified = True
    else:
        print u"验证码错误,再次尝试..."
        # print(r.content.decode('utf-8'))
        verified = False
    return verified

def get_parse_post_captcha(s,id):
    print u"获取验证码...."
    save_pic_name = get_and_save_captcha_pic(s,id)
    # print u"解析验证码..."
    text = parse_captcha_pic(save_pic_name)
    print u"解析的结果是：",text
    verified = post_captcha(s,text)
    flag = False
    if verified:
        flag = True
        print u"验证成功！继续爬取"
    else:
        get_parse_post_captcha(s,id)
    return flag


def parse_pages(html_page):
    soup = BeautifulSoup(html_page,"lxml")
    #get course numbers
    course_all_num_string = soup.find('span',class_="course-all-num").string
    course_all_num = str(re.findall(r'\d+',course_all_num_string)[0])
    #get course prices
    price = soup.find('span',class_='price').string
    return course_all_num,price


def crawlling_data(s,id):
    get_status_code,html_page = get_pages(s,id)
    if get_status_code == 200:
        classnum,price = parse_pages(html_page)
    elif get_status_code == 302:
        get_parse_post_captcha(s,id)
        classnum,price = crawlling_data(s,id)
    return classnum,price

def main():
    with requests.Session() as s:
        for i in range(1,56):
            classnum,price = crawlling_data(s,i)
            print('id: ',str(i),'classnum: ',classnum,'price: ',price)

if __name__ == "__main__":
    main()