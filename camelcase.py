import collections
import re
class stringops():
    def camelcase(self,s):
        l=[]
        cnt=0
        r=len(re.findall(r'([A-Z])',s))+1
        print(r)






s='saveChangesInTheEditor'
l1=stringops()
l1.camelcase(s)