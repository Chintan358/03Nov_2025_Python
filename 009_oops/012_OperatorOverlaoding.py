# class Calc:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __add__(self,obj):
#         return self.a+obj.a,self.b+obj.b

#     def __mul__(self,obj):
#         return self.a*obj.a,self.b*obj.b



# c1 = Calc(10,20)
# c2 = Calc(30,40)

# # k = c1+c2
# # print(k)

# k = c1*c2
# print(k)


class Calc:

    def __init__(self,*a):
        self.a = a

    def __add__(self,obj):
        k = []
        for i in range(len(self.a)):
            k.append(self.a[i]+obj.a[i])
        return k

    def __mul__(self,obj):
        return self.a*obj.a,self.b*obj.b



c1 = Calc(10,20,30)
c2 = Calc(1,2,3)
k = c1+c2
print(k)




class Test:

    def __init__(self,*a):
        pass