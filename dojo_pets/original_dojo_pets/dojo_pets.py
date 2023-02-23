class Ninja:
    def __init__(self, first_name, last_name,treats, pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats=treats
        self.pet_food= pet_food
        self. pet= pet

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self


class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy +=25
        print(f"{self.name} is sleeping! ZZZ!!!")
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health +=10
        print("NOM!! NOM!!")
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -=10
        print(f"{self.name} is playing!")
        return self

    # noise() - prints out the pet's sound 
    def noise(self):
        print("WOOF")

pickles = Pet("Mr.Pickles", "dog", "play dead")
jared = Ninja ("Jared", "Sunday","treats","pet food",pickles)

jared.walk()
jared.feed()
jared.bathe()
pickles.eat()
pickles.sleep()
pickles.play()
pickles.noise()