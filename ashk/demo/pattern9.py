a1=int(input("enter the row "))
for i in range (1,a1+1):
    for j in range(a1+1,1,-1):
        if j>i:
          print( i ,end=" ")
        else:
           print(" ",end=" ")
    print()


# a1=int(input("enter the row "))
# for i in range (1,a1+1):
#     for j in range(i,0,-1):
#       print(j,end=" ")
#     print()


# a1=int(input("enter the row "))
# for i in range (1,a1+1):
#     for j in range(1,i+1):
#          if j==i or j==1 : 
#           print("1" ,end=" ")
#          else:
#           print(i-1 ,end=" ") 
#     print()
