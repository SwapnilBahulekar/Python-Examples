#text file parsing

myfile=open(r'C:\Users\Swapnil\Documents\interviewprep\months.txt','r')
l=[]
l1=[]
l2=[]
for f in myfile.readlines():
    l.append(f.strip('\n'))
print(l)

keys=['name','surname','number']
name=['swapnil','bahulekar','1']
name1=['sagar','mane','2']
name2=['jay','patil','3']

dictlist=[]


dictlist.append(dict(zip(keys,name)))
dictlist.append(dict(zip(keys,name1)))
dictlist.append(dict(zip(keys,name2)))

print(dictlist)

for i in dictlist:
    if  'name' in i :
        #print("success")
        l2.append(i['name'])
print(l2)










