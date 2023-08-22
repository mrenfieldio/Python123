# def sample(n):
#      if n>0:
#        print("hello")
#        sample(n-1) 
# sample(10)


# def sample(n):
       
#        n1=len(n)-1 
#        print(n1)
#        if n1>=0:
#           print(n[n1])  
          

# n=input("enter a string ")
       
# sample(n) 


def dis(s):
   s1=len(s)
   if s1>0:
      b1=""
      b1+=s[s1]
      print(b1,end=" ")
      dis(s1-1)
dis("python")

# sum=0
# def dis(a1):
#      if a1>0:
#       global sum
#       sum+=a1    
#       dis(a1-1)
# a1=int(input("enter a number "))
# dis(a1)
# print("sum of the numbers",sum)
  

# sum=1
# def dis(a1):
#      if a1>0:
#       global sum
#       sum*=a1    
#       dis(a1-1)
# a1=int(input("enter a number "))
# dis(a1)
# print("sum of the numbers",sum)
  
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))