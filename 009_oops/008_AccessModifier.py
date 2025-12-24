# class Emp:
#     def __init__(self,name):
#         self.name = name

# e = Emp("Sneha")
# print(e.name)


# class Emp:
#     def __init__(self,name):
#         self._name = name

# class Company(Emp):

#     def display(self):
#         print("Emp : ",self._name)

# e = Emp("Sneha")
# print(e._name)

# c = Company("abc")
# c.display()
# print(c._name)



class Emp:
    def __init__(self,name,email,phone):
        self.__name = name
        self._email = email
        self.phone = phone



e = Emp("Sneha","sneha@gmail.com",7485968574)
print(dir(e))
print(e.phone)
print(e._email)
print(e._Emp__name)

