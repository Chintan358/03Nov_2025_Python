class Demo:

    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b
        # print("Demo construcor calling")

    def __init__(self,a):
        self.a = a

    # def __str__(self):
    #     return "Hello"

    def __eq__(self, value):
        return self.a==value.a and self.b == value.b
    
    def __len__(self):
        return len(self.a)
    
    def __setitem__(self,key,value):
        self.a[key] = value

    def __getitem__(self,key):
        return self.a[key]

# d1 = Demo(10,20)
# d2 = Demo(10,20)
# print(d1==d2)

d = Demo([10,20,30,40])
# print(len(d))
# d[1] = 10
# print(d.a)

print(d[2])