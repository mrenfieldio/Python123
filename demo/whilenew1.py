# a1=input("enter a sentence ")
# a2=a1.split()
# i=0
# while i<len(a2):
#     if 'e' in a2[i]:
#         print(a2[i])
#     i+=1

# l=[]
# for i in range(0,5):
#    a1=int(input("enter list of number "))
#    l.append(a1)
# j=0

l=[]
sum=0
avg=0
for i  in range(1,5):
    a1=int(input("enter some numbers "))
    l.append(a1)
for j in l:
    sum+=j
avg=sum/len(l)
print( "average is",avg)
x=0
print("number greater than average")
while x<len(l):
    if l[x]>avg:
     print(l[x])
    x+=1



