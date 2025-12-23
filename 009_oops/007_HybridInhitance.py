class A:

    def a(self):
        print("a calling")

class B(A):

    def b(self):
        print("b calling")
    
    def a(self):
        print("a calling - b overide")

class C(A):

    def c(self):
        print("c calling")

    def a(self):
        print("a calling - c overide")

class D(C,B):

    def d(self):
        print("d calling")
        

d = D()
d.d()
d.a()
d.b()
d.c()