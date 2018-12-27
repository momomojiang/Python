class Animal:
    def __init__(self,name,health):
	    self.name=name
	    self.health=health
    def animal_walk(self):
	    self.health-=1
	    return self
    def animal_run(self):
	    self.health-=5
	    return self
    def display_health(self):
	    print(f"{self.name} has {self.health} health")
	    return self

class Dog(Animal):
    def __init__(self,name,health):
	    super().__init__(name,health)
	    self.health = 150
    def dog_pet(self):
	    self.health+=5
	    return self
class Dragon(Animal):
    def __init__(self,name,health):
	    super().__init__(name,health)
	    self.health = 170
    def fly(self):
        self.health-=10
        print("I am a Dragon")
        return self
class Zoo:
    def __init__(self, zoo_name,):
	    self.animals = []
	    self.name = zoo_name
    def addDog(self, name):
	    self.animals.append( Dog(name,health) )
    def addDragon(self, name):
	    self.animals.append( Dragon(name,health) )
    def printAllHealth(self):
	    print("-"*30, self.name, "-"*30)
	    for animal in self.animals:
		    animal.displayHealth()
zoo1 = Zoo("John's Zoo")
zoo1.addDog("Tracy")
zoo1.addDog("Doggy")
zoo1.addDragon("Draggy")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()


animal1=Animal("Tom",100)
animal1.animal_walk().animal_walk().animal_run().animal_run().animal_run().display_health()


dog=Dog("Kiki",80)
dog.animal_walk().animal_walk().animal_run().animal_run().dog_pet().dog_pet().display_health()

dragon=Dragon("Wiwi",150)
dragon.display_health()


