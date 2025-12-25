class A:

    def __display(self):
        print("Class A display calling")

class B(A):
    
    def display(self):
        print("class B display calling")

b = B()
# print(dir(b))
b._A__display()
b.display()