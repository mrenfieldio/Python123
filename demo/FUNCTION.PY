bank = {
  "acnt-number": 12345,
  "name": "ashish",
  "bank-name": "SBI"
  }
bal=0
def details():
    for x,y in bank.items():
        print(x,y) 
def deposit(n):
     global bal
     bal+=n 
     print(bal)  
def balance():
    print("balance amount",bal)     
def withdrawl(w):
     global bal
     if w>bal:
        print("insuf")
     else:
        bal-=w
        print(bal,"debited")
while True:
 print("choose the option below")
 print("Choose 1 for Deposit")
 print("choose 2 for Withdrawel")
 print("choose 3 for Check balance")
 print("choose 4 for quit") 
 b1=int(input(""))
 if b1==4:
    print("please visit again")
    break
 else:
    num=int(input("enter your account number correctly "))
    if bank["acnt-number"]==num:
        details()
        if b1==1:
            n=int(input("enter the amount to deposit "))
            
            deposit(n)
            print("amount credited")
        elif b1==2:

            w=int(input("enter the amount to withdraw "))
            withdrawl(w)
        elif b1==3:
            balance()
    

    else:
     print("wrong data")
 
 











