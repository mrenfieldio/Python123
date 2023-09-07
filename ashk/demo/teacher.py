class school:
    def __init__(self,n1,n2):
        self.name = n1
        self.dep = n2
    def teacher(self):
        print(self.name)
        print(self.dep)
        print("salary is 10000$")
    def student(self):
        print(self.name)
        print(self.dep)
        print("enrollenment number is 123 ") 
n1=input("enter your name ")
n2=input("enter yor department ")
ob=school(n1,n2) 
ob.teacher()
ob.student()
