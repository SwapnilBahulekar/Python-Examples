import csv
coord = []
rows=[]
with open(r"C:\Users\Swapnil\Documents\pythonexamples\gpstrack.txt", "r") as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        rows.append(row)
        #print(rows)
        for i in rows:
            #print("in rows")
            if str('lat') in i:
               #print("\nsuccess")
               latindex=(i.index('lat'))
               longindex=(i.index('long'))
            latval=i[latindex]
            longval=i[longindex]
               #longindex=(i.index('long'))
            coord.append([latval,longval])
    print(coord)
        #if str("lat") in rows:





           #for i in l:

           #print(latindex)

'''for i in range(0,len(f0)):
    fo=f.readline()
    print(fo)
'''
