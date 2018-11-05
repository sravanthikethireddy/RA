# import xlrd,os,string,pickle,time,requests
# # from googlecl import search
# import googleapiclient
# # print os.chdir("/home/sravanthi/Desktop/RA")
# # print os.getcwd()
# # import GoogleScraper
# file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Researchers_List_Required_Format.xlsx"
# workbook = xlrd.open_workbook(file)
# sheet = workbook.sheet_by_index(0)
# researchers = []
# urls=[]
# univ = []
# details = {}
# sites=[]
#
# # for row in range(sheet.nrows):
# #     researchers.append(sheet.cell(row,0).value)
# #     # time.sleep(1)
# # time.sleep(1)
# # for each in researchers[1:2]:
# #     val = each.split()
#     # print each
#     # time.sleep(10)
# # print len(researchers)
# # import os
# # import selenium.webdriver as webdriver
# # from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# # from selenium.webdriver.common.keys import Keys
# # chromedriver = "C:\Users\Sravanthi Kethireddy\Downloads\chromedriver_win32\chromedriver"
# # os.environ["webdriver.chrome.driver"]=chromedriver
# # def get_Results(term):
# #
# #     driver = webdriver.Chrome(chromedriver)
# #     driver.get("http://www.google.com")
# #     link = driver.find_elements_by_tag_name("a")
# #     elems = driver.find_elements_by_xpath("//h3[@class='r']")
# #     # elems = link.get_attribute("href")
# #     for elem in elems:
# #         print elem.get_attribute("href")
#
# # get_Results("david smith northeastern")
# # import linkGrabber
# # import re
# # links = linkGrabber.Links("https://www.google.com/#q=david,+smith+northeastern")
# # gb = links.find(limit=20, pretty=True)
# # print gb
# # from BeautifulSoup import BeautifulSoup
# # import urllib2
# # import re
# #
# # html_page = urllib2.urlopen("https://www.google.com/#q=david,+smith+northeastern")
# # soup = BeautifulSoup(html_page)
# # links = []
# #
# # for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
# #     links.append(link.get('href'))
# #
# # print(links)
# from google import search
# import requests,pickle
# # ip = "david, smith northeastern"
# for each in researchers[1:50]:
#     ip = each + "northeastern"
#     time.sleep(2)
#     for url in search(ip, stop=1, num=1):
#         time.sleep(2)
#         r = requests.get(url)
#         if "pdf" not in url:
#             details[each]=url
#
# pickle.dump(details,open("details.p","wb"))
import pickle
# dict = pickle.load(open("list_1.p","rb"))
# for each in dict.items():
#     print each
cvs = {}
with open('resumes_400.p','rb') as f:
    cvs.update(pickle.load(f))
with open('resumes_800.p','rb') as f:
    cvs.update(pickle.load(f))
# with open('pdf_3.p','rb') as f:
#     cvs.update(pickle.load(f))
# with open('pdf_4.p','rb') as f:
#     cvs.update(pickle.load(f))
# with open('list_5.p','rb') as f:
#     cvs.update(pickle.load(f))
import csv
with open('resume.csv','wb') as output:
    writer = csv.writer(output)
    for key, value in cvs.iteritems():
        writer.writerow([key,value])