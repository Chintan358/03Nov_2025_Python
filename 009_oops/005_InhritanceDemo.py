class A:

    def __init__(self):
        print("A const calling")

    def display(self):
        print("Runing A")

class B : 

    def __init__(self):
        print("B const calling")

    def display(self):
        print("Running B")

class C(A,B):

    def __init__(self):
    #   super().__init__()
        A.__init__(self)
        B.__init__(self)

    def display(self):
        print("C calling")
        B.display(self)
        A.display(self)

c = C()
c.display()


#multilevel
# class C(B):

#     def test(self):
#         print("runing C")

#multiple
# class C(A,B):

#     def test(self):
#         print("runing C")

# Hierarchical
# class C(A):

#     def test(self):
#         print("runing C")