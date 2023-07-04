import re
fh=open('regex_sum_1791837.txt')

numlist=list()
som=0
for line in fh :
    lne=line.rstrip()
    num=re.findall('[0-9]+',lne)
   
    for n in num:
        #print("eachnumb",(n))
        som=som+int(n)
        #print("Add",som)
    
    
    
     

print(som)