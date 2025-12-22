class Student:

    clg = "DRSTC"
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

    def display(self):
        print(self.__class__.clg)
        print(self.id, self.name, self.email,self.clg)

    @classmethod
    def show(cls):
        print(cls.clg)

    @staticmethod
    def util():
        print("static method calling")


# Student.clg="ABC"

# st = Student(10,"Dev","dev@gmail.com")
# st.display()

# st1 = Student(11,"parth","parth@gmail.com")
# st1.display()

# Student.show()

# Student.util()

# import sys
# import gc
# st = Student(10,"jj0","ccc")
# st = [10,20,30,40]
# y = st
# st1 = y
# print(sys.getrefcount(st1))