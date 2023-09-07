'''a1=int(input("enter your age "))
a2=input("enter the day ")

b1=a2.lower()
if a1<12 or a1>65 :
    print("ticket cost is $5")
elif a1>=12 and a1<=18 and b1=="wednesday" :
    print("ticket cost $4")
else :
    print("ticket cost is $8") '''

'''num=int(input("enter the purchase amount "))  
if num>=100 :
    num1=num-num*10/100
    print(num1)
elif num<100 :
    print("price is",num,"no discount")'''

i=0
question1= {
    "1.who is the father of nation" :"a.gandhi b.manu c.rahul d.ashish"

}
print(question1)
a1=input("input your answer ")
a2=a1.lower()
if a2== "a":
    print("answer is correct")
    n=i+1
    print("score =",n)
else:
    print("answer is false")
    n=i-1
    print("score =",n)
    







    
