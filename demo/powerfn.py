# def sample(n):
#   return n**2
# data = [1, 2, 3, 4, 5]   
# print(list(map(sample,data)))

# data = [1, 2, 3, 4, 5] 
# result1 = map(lambda x: x**2, data)  
# print(list(result1))

# def sample(n):
#   return n%2==1
# data = [1, 2, 3, 4, 5]   
# print(list(filter(sample,data)))

# data=[1,2,3,4,5]
# x=filter(lambda a:a%2==1,data)
# print(list(x))

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# def sample(* abc):
#     return abc[0]+abc[1]
# print(reduce(sample,l))

# from functools import reduce
# l=[1,2,3,4,5]
# print("factorial of 5 is ")
# def sample(*abc):
#     return abc[0]*abc[1]
# print(reduce(sample,l))

# data=[-1,2,-3,4,-5]
# x=filter(lambda a:a>0,data)
# print(list(x))

# def sample(a):
#     return a>0
# data=[-1,2,-3,4,-5]
# print(list(filter(sample,data)))

# data="Python"
# x=map(lambda a:a.upper(),data)
# print("".join(list(x)))

# def sample(n):
#     return n.upper()
# data="python"
# print(" ".join(map(sample,data)))


# l=['a','e','i','o','u']
# data=input("enter a string ")
# x=filter(lambda a:a in l,data)
# print(" ".join(list(x)))

a1=input("enter a string ")
def sample(a):
    return a in l
l=['a','e','i','o','u']
print(" ".join(filter(sample,a1)))
