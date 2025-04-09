class Dog: # this defines a class which means there are multipe objects inside it OOP object oriented programing 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # this is an atribute its like an object but whenever the object is caled this will happen it helps in defining multiple instances

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    
    def set_name(self, name):
        self.name = name
    # these modify the already set ones in __init__

    def add_one(self, x):
        return x + 1
    # this is an object of dog can be called a method

    def bark(self):
        print("bark")
    # this is an object of dog can be called a method

dog = Dog("Max Park", 12)
dog.set_age(100)
dog.set_name("Sacred Dog")
print(dog.get_age())
print(dog.get_name())


