import xlrd,pickle,time,requests
from selenium import webdriver
from bs4 import BeautifulSoup
import BeautifulSoup as bs4
file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Res.xlsx"
workbook = xlrd.open_workbook(file)
sheet = workbook.sheet_by_index(0)
researchers = []
names =[]
details={}
i=1
for row in range(sheet.nrows):
    researchers.append(sheet.cell(row, 0).value)
driver = webdriver.Firefox()
def find_univ_web():
    i=1

    for each in researchers[1:3]:
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

            if "pdf" not in href:
                details[each]=href
                print i,":",each
            else:
                details[each]="No university website found"
            i+=1

        except IndexError:
            pass
    pickle.dump(details,open("test.p","wb"))

def find_phd():
    page = requests.get("https://bouve.northeastern.edu/directory/amy-briesch/")
    # result = requests.get()
    c = page.content
    soup = BeautifulSoup(c)
    article_text =''
    article = soup.findAll('p')
    for ele in article:
        article_text += '\n'+''.join(ele.findAll(text=True))
    print article_text
    # for line in article_text:
    if "PhD" or "phd" or "Ph.d" in article_text:
        print article_text
# find_phd()
import string,re
from BeautifulSoup import BeautifulSoup, SoupStrainer
for each in researchers:
    name = re.sub('[^a-zA-Z\d\s]','',each)
    names.append(name)
import httplib2,urllib2
def get_personal_sites():
    i=1
    driver = webdriver.Firefox()
    for each in names[1:4]:
        name = each.split()
        try:
            search = "https://www.google.com/search?q=" + name[0] + "+" + name[1] + "+" + "northeastern"
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
            request = urllib2.Request(search,headers=hdr)
            response = urllib2.urlopen(request)
            soup = BeautifulSoup(response)
            for a in soup.findAll('a'):
                if name[0] or name[1] in a['href']:
                    if "northeastern" not in a['href']:

                        print a.get('href')

            i+=1
        except IndexError:
            pass

# find_univ_web()
# pdfs = {}
def find_cv():
    i=1
    for each in researchers[401:]:
        try:
            name = each.split()
            search = "https://www.google.com/search?q=" + name[0] + "+" + name[1] + "+" + "northeastern"
            time.sleep(1)
            # print search
            driver.get(search)
            # res = driver.find_elements_by_css_selector('div.g')
            # link = res[0].find_element_by_tag_name("a")
            # href = link.get_attribute("href")
            href = [link.get_attribute("href") for link in driver.find_elements_by_css_selector('div.g a')]

            for h in href:
                if h is None:
                    continue
                    # else:
                    #     pdfs[each]="no cv found"
                if "cv" or "CV" in h:
                    if "pdf" in h:
                        pdfs[each]=h
                        print i, each
                        break
                    else:
                        pass


            i+=1

        except IndexError:
            pass
    pickle.dump(pdfs, open("resumes_800.p", "wb"))
# find_cv()
# p = pickle.load(open("resumes_800.p","rb"))
# for pp in p.items():
#     print pp