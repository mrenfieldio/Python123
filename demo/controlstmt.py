# for i in range (1,6):
#     if i==3:
#      continue
#     print(i)
# l=[]   
# j=0
# while j>=0:
#     a1=int(input("enter the numbers "))
#     l.append(a1)
#     if a1<0:
#         print(l)
#         break
#     j+=1


# print("enter a number between 1 to 100")
# l=[]   
# j=0
# while j>=0:
#     a1=int(input("enter the numbers "))
#     l.append(a1)
#     if a1>100 or a1<1:
#         break
#     else:
#         print(l)
#     j+=1
  
# j=0
# while j>=0:
#     a1=int(input("enter the numbers "))
#     if a1==100:
#         print("you got it")
#         break
#     j+=1

# l=['a','e','i','o','u']
# a1=(input("enter a string "))
# a2=a1.lower()
# for x in a2:
#      if x in l:
#           continue
#      print(x ,end=" ")


list1=["apple","orange","avacado"]
emp=[]
i=0
print("items are:apple,orange,avacado.\nEnter the item you want")
print("Enter Q for quit")
while True:
   a=input("enter:: ")
   if a == 'Q':
      break
   else:
      if a not in list1:
         print("enter correct item:")
         continue
      emp.append(a)

      if emp.count(a)>1:
         print("invalid input")
         break
i+=1