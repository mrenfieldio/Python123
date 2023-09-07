# x= 0
# for i in range(5):
#     for j in range(5):
#         print(chr(65 + x), end=" ")
#         x += 1
#     print()

# for i in range(65,69):
#     for j in range(5):
#         print(chr(i ), end=" ")
#     print()

# for i in range(4):
#    for j in range(0,4):
#         print(chr(j+65 ), end=" ")
#    print()


for i in range(0,4):
    for j in range(i+1):
         print(chr(j+65), end=" ")
    print()