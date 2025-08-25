class Person1:
    def __init__(self):
        self.name = "Mike"
        self.age = 25


person1 = Person1()
print(person1.name)
print(person1.age)

class Person:
    
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    def __del__(self):
        print("Object deleted!")
        Person.amount -= 1
    
    def __str__(self):
        return("Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height))

    def get_older(years):
        self.age += years
person2 = Person("John", 30, 180)
print(person2.name)
print(person2.age)
print(person2.height)

del person2

person3 = Person("Sara", 39, 175)

print(Person.amount)
