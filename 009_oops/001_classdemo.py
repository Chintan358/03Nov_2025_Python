class Pen:

    price = 10
    color = "RED"

    #function member
    def to_write(self):
       
        print("Writing something...")
        print(self.price,self.color)

    def display(self):
        print(self.price,self.color)

p1 = Pen()
p1.price=100
p1.color="Black"
p1.to_write()


p2 = Pen()
p2.price=150
p2.to_write()



# p3 = Pen()
# p3.display()