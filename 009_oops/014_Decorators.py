
# def before(func):
#     def execute():
#         print("calling before test")
#         func()
#     return execute

# def after(func):
#     def execute():
#         func()
#         print("calling after test")
       
#     return execute

# def test():
#     print("Test calling")
# test()


# def add(func):
#     def execute(*a):
#         func(*a)
#         sum = 0
#         for i in a:
#             sum+=i
#         print(f"sum is  : {sum}")        
#     return execute


# def mul(func):
#     def execute(*a):
#         func(*a)
#         sum = 1
#         for i in a:
#             sum*=i
#         print(f"mul is  : {sum}")        
#     return execute

# @add
# @mul
# def calc(a,b):
#     print("calc calling...")

# calc(10,20)


# def setdata(data):
#     print(data)

# setdata(ffd)


def numbersOnly(func):
    def execute(a):
        if str(a).isdigit():
            func(a)
        else:
            print("Invalid input")
    return execute


def charOnly(func):
    def execute(a):
        if str(a).isalpha():
            func(a)
        else:
            print("Invalid input")
    return execute



@charOnly
def data(value):
    print(value)


data("123")