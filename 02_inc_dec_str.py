from math import ceil as c
class solution :
   def sortString(self,st:str) -> str:
        p =[0]*26
        for i in st:
           p[ord*(i)-97]+= 1
        s = " "
        k = sim(p)
        while(k!=0):
            for i in range(26):
                if(p[i]!=0):
                    s+= chr(i+97)
                    p[i]-= 1
                    k-=1
            if(k == 0):
                break
            else:
                for i in range(25,-1,-1):
                    if(p[i]!=0):
                        s+= chr(i+97)
                        p[i]-=1
        return s
