# f=open("kalfan.txt","w")
# f.write("hello \n")
# f.write("world")
# f.close() 

# f=open("sample12.txt","r")
# r=f.read()
# print(r)
# f.close() 

# import os
# os.remove("sample12.txt")


# import shutil
# a=r"C:\Users\Software-4pm\Desktop\ashish\ashk\demo\anu.txt"
# b=r"C:\Users\Software-4pm\Desktop\ashish\ashk"
# shutil.move(a,b)

import shutil
b=r"C:\Users\Software-4pm\Desktop\ashish\ashk\demo"
a=r"C:\Users\Software-4pm\Desktop\ashish\ashk\anu.txt"
shutil.copy(a,b)