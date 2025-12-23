class Animal:
    name = "Generic"
    def voice(self):
        print("Genric voice")

class Cat(Animal):

    def display(self):
        print("name : ",self.name)

c = Cat()
c.name="Cat"
c.display()