a1=int(input("enter the row "))
for i in range (1,a1+1):
    for j in range(1,i+1):
        print(2*i+1,end=" " )
    print()

    a1=int(input("enter the no : "))
for i in range (1,a1+1,2):
    for j in range(1,a1+1):
        if j<=i and j%2!=0:
         print(j,' ',end=" " )
    print()