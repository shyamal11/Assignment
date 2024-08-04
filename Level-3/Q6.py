# Single Inheritance 

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()  
dog.bark()   


# Multiple 

class Animal:
    def speak(self):
        print("Animal speaks")

class Pet:
    def play(self):
        print("Pet plays")

class Dog(Animal, Pet):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()  
dog.play()   
dog.bark()   


# Multilevel

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()  
dog.walk()   
dog.bark()   

