a1=input("enter some words with special character ")
a2=[]
a3=[]
for i in a1:
    a2.append(i)
    if i.isalnum():
        a3.append(i)
    else:
        pass
print(a3)
   
     