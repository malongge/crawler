#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import unicodecsv as csv
import re
import threading

#for demonstration:set quenuenum = 10 or 50
queuenum = 3
# save_file_name = "result-multithreading-200-1.csv"
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

class crawlling_xes(threading.Thread):
    def __init__(self,id,queue):
        threading.Thread.__init__(self)
        self.id = id
        self.queue = queue

    def get_pages(self,id):
        url = "http://47.52.164.88/test.php?id="+str(self.id)

        try:
            # print 'crawlling: '+str(self.id)
            r = requests.get(url, proxies=proxies,headers=headers)
            # r = requests.get(url,headers=headers)
            result = r.content.decode('utf-8')
            # print(r.status_code)
        except requests.exceptions.RequestException as e:
            print(e)
            print('retring'+str(i))
        return result

    def parse_pages(self,html_page):
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
        result.append(self.id)
        result.append(course_name)
        result.append(course_all_num)
        result.append(price)
        result.append(teacher_pic)
        return result
    
    def write_data(self,result_list):
        if len(result_list)!=0:
            with open(save_file_name,'ab') as resultFile:
                wr = csv.writer(resultFile,dialect='excel',encoding='utf_8')
                wr.writerow(result_list)
        else:
            print 'NO DATA'
    
    def run(self):
        with self.queue:
            html_page = self.get_pages(self.id)
            result = self.parse_pages(html_page)
            # result.insert(0,i)
            course_all_num = result[2]
            price = result[3]
            print u"课程id：",str(self.id),u"课程数目：",course_all_num,u"课程价格：",price
            # self.write_data(result)


if __name__ == "__main__":
    threadingSum = threading.Semaphore(queuenum)
    for i in range(1,201):
        t = crawlling_xes(i,threadingSum)
        t.start()
    
    for t in threading.enumerate():
        if t is threading.currentThread():
            continue
        t.join()