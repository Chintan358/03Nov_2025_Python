# st = {10,20,30,40,50,50,True,1}
# st = set((10,20,30,40,50,50,True,1))
# print(st)

# if 200 in st:
#     print("20 is present in set")

# st.add(100)
# st.add(200)
# print(st)

# st1 = {60,70,80,90,100}
# st1 = [60,70,80,90,100,500,500]
# st.update(st1)
# print(st)

# st.remove(200)
# st.discard(200)


# st.pop()
# print(st)

# k = {"apple","mango","banana","grapes","orange"}
# # k.pop()
# k.clear()
# del k
# print(k)

# for item in k:
#     print(item)


A = {10,20,30,40,50,True}
B = {40,50,60,70,80,1}

# A.update(B)
# print("After update A:",A)
# C = A.union(B)
# print(C)

# C = A.intersection(B)
# print("Common elements:",C)
# A.intersection_update(B)
# print("After intersection update A:",A)

# C = A.difference(B)
# print("Elements in A not in B:",C)
# A.difference_update(B)
# print("After difference update A:",A)

# C = A.symmetric_difference(B)
# print("Elements in A and B but not in both:",C)
# A.symmetric_difference_update(B)
# print("After symmetric difference update A:",A)


# C = A | B
# print("Union using | operator:",C)
# C = A & B
# print("Intersection using & operator:",C)
# C = A - B
# print("Difference using - operator:",C)
# C = A ^ B
# print("Symmetric Difference using ^ operator:",C)

# x = frozenset((10,20,30,40,50,60))
# y = set(x)
# y.add(70)
# x = frozenset(y)
# print(x)

# s = {"A", "B", "C"}
# k = s.copy()
# print("Original set:", s)
# k.add("D")
# print("Copied set after adding D:", k)


A = {1, 2, 3,4,5,6}
B = {4, 5, 6}
print(A.isdisjoint(B))  # True, as there are no common elements
print(B.issubset(A))    # False, as not all elements of A are in B

print(A.issuperset(B))  # True, as A contains all elements of B