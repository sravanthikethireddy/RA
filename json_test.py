import csv,json,sys
maxInt = sys.maxsize
print maxInt
csv.field_size_limit(2147483647)
# path = "C:\Users\Sravanthi Kethireddy\Desktop\RA\data (1)"
path = "C:\Users\Sravanthi Kethireddy\Desktop\RA\linkedin"
with open(path+'\data.csv') as f:
# with open('education.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
with open('linkedin_details.json','w') as f:
    json.dump(rows,f)


import json,sys
import os,re,ast
reload(sys)
sys.setdefaultencoding('utf-8')
# path= os.getcwd()+'\education.json'
# jdata=open('education.json')
jdata = open('linkedin_details.json')
s_d = json.load(jdata)
jdata.close()
# details = {}
names = []
ed = []
# try:
i=1
for e in s_d:

    for a,b in e.items():
        # print a
        if a =='identifier':
            # print b
            # b.decode('ascii','ignore')
            names.append(b)
        if a=='education':

            value= b[1:len(b)-1]
            # print len(value)
            dic = ast.literal_eval(b)
            # dic = dic[0]
            # print len(dic.keys())
            print i,':', dic
            ed.append(dic)

            # for heading, details in dic[0].items():
            #     print heading,':', details
            i+=1

    # print names, ed
# except SyntaxError:
#     pass
details = dict(zip(names,ed))
# for x,y in details.items():
#     for ea in y:
#         print x, ea

# print details['Rachael Louise Wass']
# print details
# for x,y in details.items():
#     print x,";",y
# with open('json_test.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in details.items()]
import csv

# print ed


# with open("json_test.csv",'wb') as f:
# #     # writer = csv.DictWriter(f, ed[0].keys())
#     writer = csv.DictWriter(f, fieldnames=["","start","end","name","profile_url","summary","degrees"])
#     writer.writeheader()

# print details
import pandas as pd
df_list = []
for name,val in details.items():
    # print name
    df = pd.DataFrame.from_dict(details[name])
    df.index = [name]*len(df)
    # print df.index
    df_list.append(df)
    # with open("my_file.csv",'a') as f:
    #     df.to_csv(f)
    # df_list.append(df)
pd.concat(df_list).to_csv('linkedin_data_details.csv')

