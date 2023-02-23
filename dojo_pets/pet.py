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