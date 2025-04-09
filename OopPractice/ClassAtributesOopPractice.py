class Person():
    number_of_people = 0 # this doesn't have self which makes it work for the entire class not a singular thing like name

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod # this is to show python that this method is for the class not an object
    def number_of_people_(cls): # cls = class
        return cls.number_of_people
    # calling cls not self makes this work for the class not an object

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Omar")
p2 = Person("Malak")
print(Person.number_of_people_())

Person.number_of_people = 8
print(p2.number_of_people) #= 8
# notice how this gave out 8 even though we didn't change it for p2 but because this is general we managed to change it using Person which changed it for the whole class