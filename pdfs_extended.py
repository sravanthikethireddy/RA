import xlrd,pickle,time,requests,urllib2
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import *
import BeautifulSoup as bs4
file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\\D'more-Mckim.csv"
d={}
import csv,re
import lxml.html as html

with open(file) as f:
    my = dict(csv.reader(f))

for name, site in sorted(my.items()):
    if site!="No university website found":
        # time.sleep(1)
        r = requests.get(site).content
        html_obj = html.fromstring(r)
        # my_text = " ".join(
        #     [text.strip() for text in html_obj.xpath('//*[contains(.,"Curriculum Vitae")]/a/@href')])
        soup = BeautifulSoup(r)
        for a in [d for d in soup.find_all("a") if d.text=="Curriculum Vitae"]:
            print name,',', a['href']
        # for each in my_text:
        #     if "pdf" in my_text:
        #         print name, "http://www.northeastern.edu/law"+my_text[5:]
        #         break
    else:
        d[name] = "NA"

