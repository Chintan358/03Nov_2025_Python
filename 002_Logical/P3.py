# 1
# 23
# 456
# 78910

# 1
# 12
# 123
# 1234
# 12345

# 5
# 45
# 345
# 2345
# 12345

# 0
# 10
# 010
# 1010
# 01010


# for i in range(1,6):
#     for j in range(1,i+1):
#         if i%2==j%2:
#             print("0",end="")
#         else:
#             print("1",end="")
#     print()


for i in range(1,6):
    for j in range(1,i+1):
       print((i+j)%2,end="")
    print()
