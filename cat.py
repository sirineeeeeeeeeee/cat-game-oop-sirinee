#Our Cat Entity
class Cat:
    #The constructor
    #-the constructor will create a cat for us in code
    #-to create a cat, we need a given name and a given colour
    #-self is the cat we are creating
    def __init__(self,given_name,given_colour):
        #Name attribute
        self.name=given_name
        # Colour attribute
        self.colour=given_colour
        self.age=1
        self.energy=50
        self.intelligence=5
        self.weight=5
    #now we're doing methods which get included in the class!
    def train(self):
        print(f"{self.name} is training...(^=˃ ~ ˂=^)")
        self.energy -=5
        self.intelligence += 1
        self.weight += 0.1

    def feed(self):
        print(f"{self.name} is eating...(^owo^)")
        self.energy +=10
        self.weight += 1
        self.age == 0.1
