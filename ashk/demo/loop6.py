# a1=int(input("enter 5 number "))
# a2=int(input(""))
# a3=int(input(""))
# a4=int(input(""))
# a5=int(input(""))
# a6=[]
# for i in a1,a2,a3,a4,a5:
#     if i>0:
#         a7=i*i
#         a6.append(a7)
# print(a6)       

a1=int(input("enter 3 number "))
a2=int(input(""))
a3=int(input(""))
a6=[]
sum=0
n=0
sum1=[]
for i in a1,a2,a3:
    if i>0:
        a7=i*i
        a6.append(a7)
print(a6)

for i in a6:
      sum+=i        
print("sum of the numbers are",sum)       
