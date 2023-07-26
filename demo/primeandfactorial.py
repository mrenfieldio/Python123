# a1=int(input("enter a number "))
# count=0
# for i in range(1,11):
#     if a1%i==0 or a1==1:
#         count+=1
# if count>2:
#         print(a1,"is not a prime") 
# else:
#         print(a1,"is a prime")


# a1=int(input("enter a number "))
# sum=1
# for i in range(1,a1+1):
#     sum*=i
# print("factorial of ",a1,"is",sum)


a1=int(input("enter a limit to print prime numbers "))
a2=int(input(""))
count=0
for i in range(a1,a2+1):
    for j in range(1,10):
      if i%j==0 or a1==1:
        count+=1 
    if count>2:
        print(i,"is not a prime") 
    else:
        print(i,"is a prime")

