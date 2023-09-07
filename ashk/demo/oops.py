# class sample:
#     def __init__(self,name):
#         self.c=name
#         print(self.c)
#     def disdata(self,a,b):
#         self.m=a
#         self.n=b
#         print(self.m+self.n)
# name=input("enter your name ")
# n1=int(input("enter the first number "))
# n2=int(input("enter the second number "))
# obj=sample(name)
# obj.disdata(n1,n2)

class calculator:
    def __init__(self, a,b):
        self.value1 = a
        self.value2 = b
    def sum(self):
        return self.value1+self.value2
    def diff(self):
        return self.value1-self.value2
    def mul(self):
        return self.value1*self.value2
    def div(self):
        return self.value1/self.value2
    def mod(self):
        return self.value1%self.value2
op=input("enter the operator you want like +,-,*,/,% ")       
n1=int(input("enter the first number "))
n2=int(input("enter the second number "))
if op=='+':
 obj1 = calculator(n1,n2)
 print(obj1.sum())
elif op=='-': 
 obj1 = calculator(n1,n2)
 print(obj1.diff())
elif op=='*': 
 obj1 = calculator(n1,n2)
 print(obj1.mul())
elif op=='/': 
 obj1 = calculator(n1,n2)
 print(obj1.div())
elif op=='%': 
 obj1 = calculator(n1,n2)
 print(obj1.mod())
else:
   print("wrong input")