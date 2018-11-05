import xlrd,pickle,time,requests,urllib2
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import *
import BeautifulSoup as bs4
file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Book1.xlsx"
file_1 = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Book1.csv"
file_2 = "C:\Users\Sravanthi Kethireddy\Desktop\RA\personal_sites.csv"
coe = "C:\Users\Sravanthi Kethireddy\Desktop\RA\coe_dept.csv"
workbook = xlrd.open_workbook(file)
sheet = workbook.sheet_by_index(0)
univ_sites = []
names =[]
details={}
i=1
d = {}
wb = xlrd.open_workbook(file)
# sh = wb.sheet_by_index(1)
from pandas import *
import csv
with open(file_1) as f:
    # f.readline()
    my = dict(csv.reader(f))
with open(coe) as f:
    coe_researchers = dict(csv.reader(f))
# print len(my)
# for each in coe_researchers.items():
#     print each
# for each in my.items():
#     print each
def personal_sites():
    for name, site in my.items():
        print site
        if site!="No university website found":
            time.sleep(1)
            r = requests.get(site)
            soup = BeautifulSoup(r.content,"lxml")
            for href in soup.find_all("p",{"class":"personal-site"}):
                personal = href.find('a')['href']
                print name, href.find('a')['href']
                d[name]= personal
            # val =[link.get_attribute("href") for link in data]
            # print data
        else:
            d[name]="NA"
# d=my
# for name, sites in d.items():
# personal_sites()
import re

def link():
    i=1
    for name, site in my.items():
        # link = "site"
        if site != "No university website found":
            time.sleep(1)
            r= requests.get(site)
            soup = BeautifulSoup(r.content,"lxml")
            predicates = [ {'class' : re.compile('.*personal.*')},
                           {'p' : re.compile('.*personal.*')},]
            for p in predicates:
                val = soup.find_all(**p)
                print i,name,val
            i+=1



# site = "http://www.damore-mckim.northeastern.edu/faculty/s/suarez-fernando"
# r = requests.get(site)
# soup = BeautifulSoup(r.content,"lxml")
# predicates = [ {'class' : re.compile('.*personal.*')},
#                            {'p' : re.compile('.*personal.*')},
#                {'a': re.compile('.*personal.*')}]
# for p in predicates:
#     val = soup.find_all(**p)
#     print val
# print sorted(my)[:50]
i=1
phd = {}
import lxml.html as html
def trial():
    i=1
    for name, site in (my.items()):
        try:
            if site != "No university website found":
                # time.sleep(1)
                r = requests.get(site).content
                # r = requests.get("http://www.damore-mckim.northeastern.edu/faculty/s/sarathy-ravi").content
                # soup = BeautifulSoup(r.content, "lxml")
                html_obj = html.fromstring(r)
                # my_text = " ".join([text.strip() for text in html_obj.xpath('//*[(self::h4 or self::h2 or self::h3 or self::h5 or self::p) and .="Degrees/Education"]/following-sibling::p/text()')])
                my_text = " ".join([text.strip() for text in html_obj.xpath('//*[contains(.,"Education")]/following-sibling::p/text()')])

                # for elems in soup(text=re.compile('Personal')) or soup(text=re.compile('website')) or soup(text=re.compile('personal')):
                #     # val = elems.get_attribute('href')
                #     val = elems.find_parent('a',href=True)
                #
                #     print i, name, val["href"], '\n'
                #     # print i, name, elems.parent
                #     i+=1
                # print i
                # for elems in soup(text=re.compile('PhD')):
                #     # val = elems.get_attribute('href')
                #     val = elems.find_parent('p').getText()
                #     # val = val.partition()
                #
                #
                #     print name,',', val
                #     print '-------'
                print name, ',', my_text
                i+=1
                phd[name]=my_text
        except AttributeError:
            pass
        i+=1

def get_phd():
    for name, site in (my.items()):
        try:
            if site != "No university website found":
                r = requests.get(site).content

                soup = bs4.BeautifulSoup(r,"lxml")
                header = soup.find('h4', text='Education')
                val = header.find_next_sibling('p').getText()
                print val
        except AttributeError:
            pass

# trial()
# pickle.dump(phd,open("phd_list.p","wb"))
# ff = pickle.load(open("phd.p","rb"))
# i=1
# for each in ff.items():
#     print i, each
#     i+=1
def get_pickle_phds():
    f1 = pickle.load(open("phd_2.p","rb"))
    f2 = pickle.load(open("phd_3.p","rb"))
    f3 = pickle.load(open("phd_list.p","rb"))
    f4 = pickle.load(open("ccis.p","rb"))
    # print f1
    f1 = {k: unicode(v).encode("utf-8") for k, v in f1.iteritems()}
    f2 = {k: unicode(v).encode("utf-8") for k, v in f2.iteritems()}
    f3 = {k: unicode(v).encode("utf-8") for k, v in f3.iteritems()}
    f4 = {k: unicode(v).encode("utf-8") for k, v in f4.iteritems()}

    # print f2
    # w1 = csv.writer(open("phd_1.csv","w"))
    # w2 = csv.writer(open("phd_2.csv","w"))
    # w3 = csv.writer(open("phd_list.csv","w"))
    w4 = csv.writer(open("ccis.csv","w"))
    # for key,val in f1.items():
    #     w1.writerow([key,val])
    # for key,val in f2.items():
    #     w2.writerow([key,val])
    for key,val in f4.items():
        w4.writerow([key,val])
# get_pickle_phds()
# mie={}
def get_mie():
    for name, site in (coe_researchers.items()):
        try:
            if site != "No university website found":
                r = requests.get("https://bouve.northeastern.edu/directory/ralph-loring/").content
                html_obj = html.fromstring(r)
                my_text = " ".join([text.strip() for text in html_obj.xpath('//*[.="Education:"]/following::br/text()')])

                print name, ',', my_text
                # i+=1
                # mie[name]=my_text
        except AttributeError:
            pass
        # i+=1


# get_mie()

# pickle.dump(mie,open("ccis.p","wb"))
# camd = {}
def camd_cv():
    i=1
    for name, site in my.items():
        try:
            if site!="No university website found":
                r = requests.get(site).content
                html_obj = html.fromstring(r)
                # websites = " ".join([text.strip() for text in html_obj.xpath('//*[contains(.,"curriculam")]/following::a[1]/@href')])
                # print name, websites
                # camd[name]=websites
                if "Ph.D" or "PhD" not in html_obj:
                    print i, name, site
                i+=1
        except AttributeError:
            pass
# camd_cv()
driver = webdriver.Firefox()
details = {}
keywords = ['northeastern','neu']
stop = ['google','link','researchgate','twitter','facebook','pdf']
def find_univ_web():
    count=1
    all_links = []

    for each, sites in sorted(my.items())[401:]:
        try:
            name = each.split()
            search = "https://www.google.com/search?q="+name[0]+"+"+name[1]+"+"+"northeastern"
            time.sleep(1)
            # print search
            driver.get(search)
            res = driver.find_elements_by_css_selector('div.g')
            link = res[0].find_element_by_tag_name("a")
            href = link.get_attribute("href")
            href = [link.get_attribute("href") for link in driver.find_elements_by_css_selector('div.g a')]
            for i in href:
                if "northeastern" or "neu" in i:
                    if "google" not in i:
                        if "rate" not in i:
                            if "linked" not in i:
                                all_links.append(i)

            # print all_links
            print count, name
            count+=1


            details[each]=(all_links[:10])
            # details[name]=all_links
            # all_links=[]
            # print all_links
            all_links = []
            # if "neu" or "northeastern" in href:
            #     details[each].apppend(href)
            # else:
            #     details[each]="No university website found"
            # i+=1

        except (TypeError,IndexError):
            pass
    # for a in details.items():
    #     print a
    pickle.dump(details,open("google_sites_2.p","wb"))
# find_univ_web()
a1= pickle.load(open("google_sites_1.p","rb"))
a2= pickle.load(open("google_sites_2.p","rb"))
a = a1.copy()
a.update(a2)
print len(a)
with open('all_urls.csv','wb') as output:
    writer = csv.writer(output)
    for key, value in a.iteritems():
        writer.writerow([key,value])
# for each in a.items():
#     print each