# l = [10,20,30,40,50,60]
# # for i in l:
# #     print(i)

# k = iter(l)

# print(next(k))

# def square(a):
#     for i in range(1,a+1):
#         yield i*i

# a = iter(square(5))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



l = {"a":"python","b":"java"}
k = iter(l)

print(l[next(k)])

print(l[next(k)])
