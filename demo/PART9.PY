cal=int(input("enter the first number "))
cal1=int(input("enter the second number "))
cal2=(input("enter the operator "))
add=cal+cal1
sub=cal-cal1
mul=cal*cal1
div=cal/cal1
mod=cal%cal1
if cal2=='+' :
    print("sum is",add)
elif cal2=='-':
    print("substrated value is",sub)
elif cal2=='*':
    print(mul)
elif cal2=='/':
    print(div)
elif cal2=='%':
    print(mod)
else:
    print("wrong input")
