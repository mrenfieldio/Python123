# class A:
#     def disdata(self):
#      print("hai")
#      self.__a=20  
# class B(A):
#     def putdata(self):
#      print("hello")
# class C(B):
#     def getdata(self):
#      print("how are you")
# ob=C()
# ob.disdata()
# ob.putdata()
# ob.getdata()  

class person:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def disdata(self):
     print(self.name) 
     print(self.age)
class employee(person):
    def __init__(self,salary):
     self.salary=salary
    def putdata(self):
     print(self.salary)
class manager(employee):
    def __init__(self,dep):
     self.dep=dep
    def getdata(self):
     print(self.dep)
ob2=person("manu",21)
ob2.disdata()
ob1=employee(1000)
ob1.putdata()
ob=manager("cs")
ob.getdata(3)


