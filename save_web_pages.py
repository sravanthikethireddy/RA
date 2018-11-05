import csv,os,urllib2
import os.path
directory = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Researchers_Web_Pages"
def save_webpages():
    i=1
    with open("all_urls.csv",'rb') as f:
        file_reader = csv.reader(f)
        for row in file_reader:
            i=1
            os.makedirs(directory+"\\"+row[0])
            path = "C:\Users\Sravanthi Kethireddy\Desktop\RA\Researchers_Web_Pages"+"\\"+row[0]
            print path
            for site in row[1:]:
                try:
                    response = urllib2.urlopen(site)
                    content = response.read()
                    name_of_site = "Page_"+str(i)
                    name = os.path.join(path,name_of_site+'.html')
                    print name
                    i+=1
                    with open(name,'w') as fid:
                        fid.write(content)
                    # f = open(name,'w')
                    # f.write(content)
                    # f.close()
                except (IOError, ValueError):
                    pass


# save_webpages()
import xlrd,pickle,time,requests
from selenium import webdriver
from bs4 import BeautifulSoup
import BeautifulSoup as bs4
file = "C:\Users\Sravanthi Kethireddy\Desktop\RA\ccis.xlsx"
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

    for each in researchers:
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

            # if "pdf" not in href:
            #     details[each]=href
            #     print i,":",each
            # else:
            #     details[each]="No university website found"
            # i+=1
            for a in href:
                if "linkedin" in a:
                    print each,",", a

        except IndexError:
            pass
    # pickle.dump(details,open("test.p","wb"))

# find_univ_web()
# for each in researchers:
# each = raw_input("enter:")
list = [("Pirozzi, Therese"),
("Poghosyan, Hermine"),
("Howard, Betsy"),
("Guthrie, Barbara"),
("Polcari, Ann"),
("Waszczak, Barbara"),
("Madden, Jeanne"),
("Tunik, Eugene"),
("Feldman, Kevoe Heidi"),
("Nisbet, Matthew"),
("Welles, Brooke"),
("Canossa, Alessandro"),
("Morreale, Joanne"),
("Robertson, Craig"),
("Forman, Murray"),
("Mall, Andrew"),
("Smith, Ronald"),
("McDonald, Matthew"),
("Loughridge, Deidre"),
("Price, Emmett"),
("Kindelan, Nancy"),
("Clinger, William"),
("Nita-Rotaru, Cristina"),
("Rajaraman, Rajmohan"),
("Rasala, Richard"),
("Wand, Mitchell"),
("Pavel, Misha"),
("Brodley, Carla"),
("Lee-Parsons, Carolyn"),
("Ruth, Matthias"),
("Salehi, Masoud"),
("Sznaier, Mario"),
("Cullinane, Thomas"),
("Makowski, Lee"),
("Lee-Parsons, Carolyn"),
("Smith, Wendy"),
("Godoy-Carter, Veronica"),
("Apfeld, Javier"),
("Zupanc, Gunther"),
("Lewis, Kim"),
("Bergman, Kostia"),
("Hall, Adam"),
("Mattos, Carla"),
("Manetsch, Roman"),
("Ivanov, Alexander"),
("Wales, Thomas"),
("Iacob, Roxana"),
("Agar, Jeffrey"),
("Pollastri, Michael"),
("Booth, Ray"),
("Onan, Kay"),
("Abraham, Kuzhikalail"),
("Bowen, Jennifer"),
("Rosengaus, Rebeca"),
("Vollmer, Steven"),
("Gouhier, Tarik"),
("Kimbro, David"),
("Ayers, Joseph"),
("Trussell, Geoffrey"),
("Lotterhos, Katie"),
("Grabowski, Jonathan"),
("Detrich, H William"),
("Patterson, Mark"),
("Topalov, Peter"),
("Braverman, Maxim"),
("Spring, Bryan"),
("Batishchev, Oleg"),
("Chandler, Robin"),
("McDevitt, Jack"),
("Wassall, Gregory"),
("Kim, Sungwoo"),
("Marks, Mindy"),
("Morrison, Steve"),
("Alper, Neil"),
("Cushman, Ellen"),
("Kaplan, Carla"),
("Davis, Theo"),
("Boeckeler, Erika"),
("Peterfreund, Stuart"),
("Aljoe, Nicole"),
("Lerner, Neal"),
("Goshgarian, Gary"),
("Leslie, Marina"),
("Mullen, Patrick"),
("TuSmith, Bonnie"),
("Lefkovitz, Lori"),
("Walker, Louise"),
("Fowler, William"),
("Khuri-Makdisi, Iljam"),
("Heefner, Gretchen"),
("Cresswell, Tim"),
("Ortega Guzman, Elika"),
("Buscaglia, Jose"),
("Bailey, Moya"),
("Bourns, Stacey"),
("Smead, Rory"),
("Setta, Susan"),
("Kelting, Whitney"),
("Parekh, Serena"),
("Clayton-Matthews, Alan"),
("Kuhl, Laura"),
("Hoff, Tim"),
("Kelleher, Maureen"),
("Bailey, Wendy"),
("Gal-Or, Ronen"),
("Moore, Rebekah"),
("Fitzgerald, Brian"),
("Wright, Arnold"),
("Zhang, Yue"),
("Moreno, Kimberly"),
("Nichol, Jennifer"),
("Krishnamoorthy, Ganesh"),
("Liu, Kelvin"),
("Libaers, DIrk"),
("Crane, Fredrick"),
("Mitteness, Cheryl"),
("Karim, Samina"),
("Meyer, Marc"),
("Osiyevskyy, Oleksiy"),
("Katz, Ralph"),
("Whitfield, Ronald"),
("Faleye, Olubunmi"),
("Mooradian, Robert"),
("Pichler, Pegaret"),
("Platt, Harlan"),
("Born, Jeffrey"),
("Bolster, Paul"),
("Ma, Linlin"),
("Margotta, Donald"),
("Yang, Shiawee"),
("Kale, Jayant"),
("Livanis, Grigorios"),
("Puffer, Sheila"),
("Alessandri, Todd"),
("Huselid, Mark"),
("Dunlap, Denise"),
("Barczak, Gloria"),
("Lassk, Felicia"),
("Fombelle, Paul"),
("Grinstein, Amir"),
("Mulki, Jay"),
("Sultan, Fareena"),
("Satornino, Cinthia"),
("Smith, Keith"),
("Baskerville, Marla"),
("Thoroughgood, Christian"),
("Lee, Cynthia"),
("Andre, Rae"),
("Ladge, Jamie"),
("Ellen, Parker"),
("Dencker, John"),
("Xia, Amy"),
("Lee, Yang"),
("Dias, Martin"),
("Solomon, Marius"),
("Chen, Yi-Da"),
("Riedl, Chris"),
("Sanders, Nada"),
("Scott, Alex"),
("Ambulkar, Saurabh"),
("Zepeda, David"),
("Wiseman, Frederick"),
("Nyaga, Gilbert")
]
for each in list:
    try:
        name = each.split()
        search = "https://www.google.com/search?q=" + name[0] + "+" + name[1] + "+" + "northeastern"
        time.sleep(1)
        # print search
        driver.get(search)
        res = driver.find_elements_by_css_selector('div.g')
        link = res[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        href = [link.get_attribute("href") for link in driver.find_elements_by_css_selector('div.g a')]

        # if "pdf" not in href:
        #     details[each]=href
        #     print i,":",each
        # else:
        #     details[each]="No university website found"
        # i+=1
        for a in href:
            if "linkedin" in a:
                print each, ",", a

    except (IndexError,TypeError):
        pass