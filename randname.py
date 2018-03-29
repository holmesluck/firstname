from chinesename import chinesename
# import pandas as pd
# import numpy as np
import csv

cn = chinesename.ChineseName()
# data = pd.read_csv('./1.csv')

# db1 = np.zeros([5000,2])

data = []
data1 = []
for i in range(5000):
    fname = cn.getFirstName(char_count=2)
    lname = cn.getLastName()
    dic = {'SEQ': 0, 'Firstname': ""}
    dic1 = {"SEQ":0, 'Lastname':""}
    dic["SEQ"] = i
    dic1["SEQ"] = i
    dic["Firstname"]= fname
    dic1["Lastname"] = lname
    data.append(dic)
    data1.append(dic1)
# for i in range(5000):
#         cname = cn.getName ()
#         data['SEQ'][i]= i
#         data['Firstname']= cname
#
# # print(cname)
# print(data['SEQ'][i])
# print(data)
# print(len(data))

# print(data1)
# print(len(data1))

db =[]
db1 = []
db2 = []
o=-3

csvread = csv.reader(open(r'./3.csv',encoding='utf-8'))
for row in csvread:
    db.append(row)
dbl=len(db)
# print(dbl)
for i in range(10):
 for row in db:
  db1.append(row)
  db2.append(row)
 for i in range(dbl):
    db[i][0]=o
    o+=1
    # db2[i+i*dbl][0]=db[i][0]+i*dbl
    # db2[i+i*dbl][1]=db[i][1]
    # print('('+str(db[i])+')'+',')
dbl1 = len(db1)
dbl2 = len(db2)

csv1 = open("./1.csv",'w',encoding="utf-8",newline="")
wr1 = csv.writer(csv1)
for k in range(dbl1):
    fname = cn.getFirstName (char_count=2)
    db1[k][0]= k-3
    db1[k][1]= fname
    wr1.writerow (db1[k])
csv1.close()


csv2 = open("./2.csv",'w',encoding="utf-8",newline="")
wr2 = csv.writer(csv2)
for l in range(dbl2):
    lname = cn.getLastName ()
    db2[k][0]= l-3
    db2[k][1]= lname
    wr2.writerow (db2[k])
csv2.close()


# # write in dic
# len1 = len(data)
# for i in range (data):
#  dic= data[i]
#  for key in dic:
#     db= dic[key]
#     print(db)
# print(db)
# wr1.writerow(db)
# csv1.close()