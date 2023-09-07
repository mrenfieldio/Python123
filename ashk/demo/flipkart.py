
bal=0 
def pant():
     global bal
     print("pant price is $500")
     p1=input("if you want press y to proceed ")
     if p1=='y':
         bal+=500 
     print("total amount",bal)  
def shirt():
    global bal
    print("Shirt price is $300")
    p1=input("if you want press y to proceed ")
    if p1=='y':
        bal+=300 
    print("total amount",bal)    
def  st3():
     global bal
     print("T-Shirt price is $200")
     p1=input("if you want press y to proceed ")
     if p1=='y':
        bal+=200 
     print("total amount",bal)
while True: 
 b1=int(input("choose the item you want: \n 1.shirt \n 2.pant \n 3.t-shirt \n 4.quit \n"))
 if b1==4:
    print("please visit again")
    print("total amout of purchase is ",bal)
    if bal>500:
        d1=bal*3/100
        d2=bal-d1
        print("amout to pay after discount is",d2)
    break
 else:
        if b1==2:
            pant()
            print("pant purchased")
        elif b1==1:
            shirt()
            print("shirt purchased")
        elif b1==3:
            st3()
            print("T-shirt purchased")
    