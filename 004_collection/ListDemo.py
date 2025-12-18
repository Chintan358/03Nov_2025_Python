# The code snippet you provided is demonstrating various operations that can be performed on lists in
# Python. Here is a breakdown of the operations being demonstrated:
# l = [10,20,30,40,50,10,45.56]
# print(len(l))
# print(l)
# for i in l : 
#     print(i)

# The code snippet `for i in range(len(l)): print(l[i])` is iterating over the indices of the list `l`
# using a for loop.
# for i in range(len(l)):
#     print(l[i])


# l.append("Test")
# l.insert(2,"add")
# l[2] = "Add"

# l.remove(10)
# l.pop(5)
# l.clear()
# del l

# print(l.index(500))

# print(l.count(10))

# l.sort(reverse=True)

# k = sorted(l)
# print(k)

# l.reverse()
# print(l)


# k = [10,20,30,40,50,60]

# a = []

# for i in k:
#     a.append(i*i)
# print(a)

# a = [i*i for i in k]
# print(a)

# print(k[::-1])


# a = [10,20,30]
# b = [50,60,40]
# a.extend(b)
# print(a)

# c = a.copy()
# print(c)

l = [10,20,30,40,50,60]

l[2:4] = [300,400,500]
print(l)