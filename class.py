x= 1
print(type(x))
def hello():
    print("Hello!")
print(type(hello))

#Methods
class Dog:
    voice = "Woof"
    def bark(self):
        print(self.voice)
dog = Dog()
Dog.bark()
print(Dog.voice)


#string = "Hello"
#print(string.upper())

#creating a class

class Sport:
    type = "Football"
print(Sport.type)

#creating Objects
class Person:
    name = "Bod"
bob = Person()
print(bob.name)
print(type(bob))
print(type(Person))
