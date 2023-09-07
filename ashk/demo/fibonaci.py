def FibRec(a):  
   if a <= 1:  
       return a  
   else:  
       return(FibRec(a-1) + FibRec(a-2))  
a1 = int(input("Enter the terms? ")) 
print("Fibonacci sequence:")  
for i in range(a1): 
       print(FibRec(i),end=" ")
