# 0 1 1 2 3 5 8 13 21 34 55 89 

a = 0  #1  1 2
b = 1  #1  2 3
print(a,b,end=" ")
for i in range(18):
    c  =a+b
    a = b
    b = c
    print(c,end=" ")
