class Pet: # this is a more general class which means it doesn't connect with specifics so it is perfect for inheratince
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print("I don't know what to say")
        
class Dog(Pet): 
    def speak(self):
        print("Bark!")

class Cat(Pet): # this parameter is the thing that will allow us to inhert the Pet class
    def __init__(self, name, age, color):
        super().__init__(name, age) # we use te super func to make the super or the inheritance class the same attributes as name and age to not lose anything that may be important in it
        self.color = color

    def show(self):
        print(f"I am {self.name} and i am {self.color} and i am {self.age} years old")

    def speak(self):
        print("Meow!")

# those two are closed which means they are rarley used with anything else other than dog and cat what else can do this stuff your mom ?

pet = Pet("Mark", 5)
pet.show()

cat = Cat("Phill", 6, "Yellow")
cat.show()

dog = Dog("Max", 6)
dog.show()
# notice that in both of these the show method worked even though there is no __init__ method in cat or dog that is because it inherited it from pet

cat.speak()
dog.speak()