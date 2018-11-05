import xlrd,pickle,time
from selenium import webdriver
file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Researchers_List_Required_Format.xlsx"
workbook = xlrd.open_workbook(file)
sheet = workbook.sheet_by_index(0)
researchers = []
details={}
driver = webdriver.Firefox()
for row in range(sheet.nrows):
    researchers.append(sheet.cell(row,0).value)
for each in researchers[202:]:
    try:
        name = each.split()
        search = "https://www.google.com/search?q="+name[0]+"+"+name[1]+"+"+"northeastern"
        time.sleep(2)
        # print search
        driver.get(search)
        res = driver.find_elements_by_css_selector('div.g')
        link = res[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        if "pdf" not in href:
            details[each]=href
    except IndexError:
        pass
pickle.dump(details,open("univ_Web_6.p","wb"))