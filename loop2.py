a1=['a','b','m','a','c','a','b','c']
# x=1
# count=0
# b1=[]
# for i in a1:
#      if i==a1[x]: 
#               count+=1
#               x-=1
#               if count>=2:
#                 b1.append(i) 
# a3=set(b1)
# print(a3)

c=0
d={}
for i in a1:
   
    d.update({i:a1.count(i)})

print(d)

for j in d.values():
    if j>1:
        s3=d.keys()
print(s3)
       


