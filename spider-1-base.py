#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import unicodecsv as csv
import re


proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080",
}
save_file_name = 'spider-1-base1.csv'

def get_pages(id):
    url = "http://47.52.164.88/test.php?id="+str(id)
    try:
        r = requests.get(url, proxies=proxies)
        result = r.content.decode('utf-8')
    except requests.exceptions.RequestException as e:
        print(e)
        print('retring'+str(i))
    return result

def parse_pages(html_page):
    soup = BeautifulSoup(html_page,"lxml")
    #get course names
    course_name = soup.find("div",class_="course__title").h3.string
    #get course numbers
    course_all_num_string = soup.find('span',class_="course-all-num").string
    course_all_num = str( re.findall(r'\d+',course_all_num_string)[0])
    #get course prices
    price = soup.find('span',class_='price').string
    #get url of teacher's picture
    teacher_pic = soup.find('div',class_='xue-card-subject-avatar xue-avatar-style1').span.img['src']
    result = []
    result.append(course_name)
    result.append(course_all_num)
    result.append(price)
    result.append(teacher_pic)
    return result


def write_data(result_list):
    if len(result_list)!=0:
        with open(save_file_name,'ab') as resultFile:
            wr = csv.writer(resultFile,dialect='excel',encoding='utf_8')
            wr.writerow(result_list)
    else:
        print 'NO DATA'

def main():
    for i in range(1,21):
        html_page = get_pages(i)
        result = parse_pages(html_page)
        # insert id into the first column
        # result.insert(0,i)
        # write_data(result)
        course_all_num = result[1]
        price = result[2]
        print u'课程id:',str(i),u"讲课数目:",course_all_num,u"价格：",price

if __name__ == "__main__":
    main()
