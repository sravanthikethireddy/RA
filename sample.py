from selenium import webdriver
import xlrd
file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Researchers_List_Required_Format.xlsx"
workbook = xlrd.open_workbook(file)
sheet = workbook.sheet_by_index(0)
researchers = []
driver = webdriver.Chrome()
driver.get("https://www.google.com/#q=jose+annunziato+northeastern")
results = driver.find_elements_by_xpath('//div[@class="rc"]')

print(len(results))

for result in results:
    video = result.find_element_by_xpath('.//h3/a')
    title = video.get_attribute('title')
    url = video.get_attribute('href')
    # print("{} ({})".format(title, url))
    print url
driver.quit()
import sys # Used to add the BeautifulSoup folder the import path
import urllib2 # Used to read the html document

if __name__ == "__main__":
    ### Import Beautiful Soup
    ### Here, I have the BeautifulSoup folder in the level of this Python script
    ### So I need to tell Python where to look.
    sys.path.append("./BeautifulSoup")
    from BeautifulSoup import BeautifulSoup

    ### Create opener with Google-friendly user agent
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    ### Open page & generate soup
    ### the "start" variable will be used to iterate through 10 pages.
    for start in range(0,2):
        url = "https://www.google.com/#q=david+smith+northeastern" + str(start*2)
        page = opener.open(url)
        soup = BeautifulSoup(page)

        ### Parse and find
        ### Looks like google contains URLs in <cite> tags.
        ### So for each cite tag on each page (10), print its contents (url)
        for cite in soup.findAll('href'):
            print cite
from selenium import webdriver
driver = webdriver.Firefox()
for each in researchers:
    driver.get("https://www.google.com/search?q=david+smith+northeastern")
    res = driver.find_elements_by_css_selector('div.g')
    link = res[0].find_element_by_tag_name("a")
    href = link.get_attribute("href")
    print href