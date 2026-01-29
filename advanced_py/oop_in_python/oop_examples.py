# Python OOP Examples (Encapsulation, Inheritance, Polymorphism)

# --- Encapsulation ---
class Car:
    def __init__(self, make, model):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self._odometer = 0  # protected attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def read_odometer(self):
        return self._odometer

    def drive(self, miles):
        if miles > 0:
            self._odometer += miles

my_car = Car("Toyota", "Corolla")
# print(my_car.__make)  # This would cause an AttributeError
print(my_car.get_make())
my_car.drive(100)
print(my_car.read_odometer())

print("-" * 20)

# --- Inheritance ---
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."

my_electric_car = ElectricCar("Tesla", "Model S", 100)
print(my_electric_car.get_make())
print(my_electric_car.describe_battery())

print("-" * 20)

# --- Polymorphism ---
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
