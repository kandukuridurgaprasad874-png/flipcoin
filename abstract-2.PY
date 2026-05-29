from abc import ABC,abstractmethod
class Anmial(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Anmial):
    def sound(self):
        print("Dog says:Bark")

class Cat(Anmial):
    def sound(self):
        print("cat says:Meow")

class Hen(Anmial):
    def sound(self):
        print("Hen says:kukuruku")        

d=Dog()
c=Cat()
h=Hen()
d.sound()
c.sound()
h.sound()    
        