# Python Classes Example

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Child class that inherits from Dog
class Bulldog(Dog):
    def speak(self, sound="woof"):
        return super().speak(sound)

# Create instances of the Dog class
my_dog = Dog("Buddy", 5)
print(my_dog.description())
print(my_dog.speak("bark"))

# Create an instance of the Bulldog class
my_bulldog = Bulldog("Rocky", 3)
print(my_bulldog.description())
print(my_bulldog.speak())
