class Test:

    def __init__(self,id,name):
        self.id =id
        self.name = name

    def display(self):
        print("Display calling")
        print(self.id, self.name)

t = Test(10,"abc")
t.display()

t1 = Test(20,"xyz")
t1.display()
