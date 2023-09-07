# a="python"
# i=0
# while i<len(a):
#     print(a[i] ,end=" ")
#     i+=1

# a=["p","y","t","h","o","n",1,2,3,"python"]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# a1=input("enter a string ")
# a3=a1.lower()
# a2=["a","e","i","o","u"]
# count=0
# i=0
# print("vowels are ")
# while i<len(a3):
#     if a3[i] in a2:
#         count+=1
#         print(a3[i])
#     i+=1
# print(count)

l1=["abc","a",1,11]
l2=["a",11,150.5]
l3=[]
i=0
while i<len(l1):
    if l1[i] in l2:
         l3.append(l1[i])
    i+=1
print(l3,end=" ")




