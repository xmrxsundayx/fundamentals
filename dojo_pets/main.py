import ninja
import pet

pickles = pet.Pet("Mr.Pickles", "dog", "play dead")
jared = ninja.Ninja ("Jared", "Sunday","treats","pet food",pickles)

jared.walk()
jared.feed()
jared.bathe()
pickles.eat()
pickles.sleep()
pickles.play()
pickles.noise()