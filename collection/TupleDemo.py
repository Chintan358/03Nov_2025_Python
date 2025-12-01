# t = (10,20,30,40,50,50,"abc",True)
# print(t)

# l = [10]
# print(type(l))

# t = (10,)
# print(type(t))

# k = tuple((10,20,30,40,50,50,"abc",True))
# print(k)

# l = list((10,20,30,40,50,50,"abc",True))
# print(l)


# t = (10,20,30,40,50,50,"abc",True)
# print(t[0])
# print(t[3])
# print(t[-1])
# print(t[-4])
# print(t[2:5])

# t = (10,20,30,40,50,50,"abc",True)
# l = list(t)
# l[2] = 300
# t = tuple(l)
# print(t)

# del t
# print(t)

t = (10,20,30,40,50,50,"abc",True,20,30,10,50,50)
# (a,*b,c,d,e) = t
# print(a)
# print(b)
# print(c)

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t1 = (1,2,3)
# t2 = (4,5,6)
# t3 = t1 + t2
# print(t3*2)

print(t.count(50))
print(t.index(40))