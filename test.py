import csv

data = csv.reader(open(r'C:\Users\IBM_ADMIN\Desktop\1.csv',encoding='utf-8'))
db = []
db2 = []
for row in data:
  db.append(row)
o=-3
for i in range(10):
 for i in range(len(db)):
    db[i][0]=o
    o+=1
    print('('+str(db[i])+')'+',')
# for i in range(10):
#     db2[]


data2 = open(r'C:\Users\IBM_ADMIN\Desktop\1.csv','w',encoding='utf-8',newline='')
wr = csv.writer(data2)
m = len(db2)
for i in range(m):
    wr.writerow(db2[i])
print(len(db2))
# for i in range()
data2.close()