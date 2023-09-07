l=[]
l1=[]
l3=[]
l4=[]
l5=[]
for i in range(4):
    n=input("enter 5 number: ")
    l.append(n)
for j in range(4):
    m=input("enter 5 number? ")
    l1.append(m)
print(l)
print(l1)
for x in l:
    l3.append(x)
    for y in l1:
        l4.append(y)
        if x in y:
            a5=int(x)
            l5.append(a5)
print(l5)
    

