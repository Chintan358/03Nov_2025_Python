class Pen : 

    def __init__(self,price,color):
        self.price= price
        self.color = color

    def display(self):
        print(self.color,self.price)

class Notebook(Pen):

    def __init__(self, price, color,pages):
        self.pages = pages
        super().__init__(price, color)

    def display(self):
        print(self.color,self.price,self.pages)
        super().display()

# p  = Pen(10,"REd")
# p.display()

n = Notebook(20,"Black",200)
n.display()