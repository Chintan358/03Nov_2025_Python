# def message():
#     print("Hello, good morning")
# message()


# def square(a):
#     print(f"square of {a} is {a*a}")
# square(10)
# square(5)

# def add(a,b):
#     print(f"addition of {a} and {b} is {a+b}")
# add(10,20)
# add(50,70)

# def mod(a,b):
#     c = a%b
#     return c

# a = mod(15,2)
# print(a)
# print(mod(10,2))

# def person(name,email="abc@gmail.com",phone="111111111"):
#     print(name,email,phone)

# # person("Test",8585858585)
# person("Test",phone = 8585858585)


# def add(*a):
#     sum = 0
#     for i in a:
#         sum+=i
#     print(sum)
# add(10,20,30,40,50,60,70)

# def student(**a):
#     print(a)
# student(name="tech",email="tech@gmailc.om")

# k = lambda a,b : a+b
# print(k(10,20))

# sq = lambda a : a*a
# print(sq(10))


# a = 10

# def test():
#     global a
#     a = 20
#     print(a)

# print(a)
# test()
# print(a)

# def square(a):
#     print(a*a)
#     a+=1
#     if a<20:
#         square(a)

# square(10)

# st = "Hello World Hello Python"
# l = st.split(" ")

# for i in l:
#     for k in range(len(i)-1,-1,-1):
#         print(i[k],end="")
#     print(" ",end="")