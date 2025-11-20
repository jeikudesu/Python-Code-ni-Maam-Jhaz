# PART 1 — INHERITANCE
# ==========================================

# Activity 1: Animal Inheritance
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


# Activity 2: Vehicle Class
class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

class Car(Vehicle):
    def __init__(self, brand, fuel, doors):
        super().__init__(brand, fuel) # calling parent constructor
        self.doors = doors

    def drive(self):
        self.fuel -= 1
        print(f"Driving... Fuel left: {self.fuel}")


# ==========================================
# PART 2 — ENCAPSULATION
# ==========================================

# Activity 1: Bank Account
class BankAccount:
    def __init__(self):
        self.__balance = 0 # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Activity 2: Age Validation
class Person:
    def __init__(self, age):
        self._age = None
        self.age = age # uses setter

    @property
    def age(self):
        return self._age # getter

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")


# ==========================================
# PART 3 — POLYMORPHISM
# ==========================================

# Activity 1: Printers
class InkPrinter:
    def print_document(self):
        print("Printing using ink technology...")

class LaserPrinter:
    def print_document(self):
        print("Printing using laser technology...")


# Activity 2: Duck Typing
def make_it_speak(obj):
    obj.speak() # works for any object with speak()


class Bird:
    def speak(self):
        print("Chirp chirp!")

class Robot:
    def speak(self):
        print("Beep boop!")


# ==========================================
# PART 4 — ABSTRACTION
# ==========================================
from abc import ABC, abstractmethod

# Activity 1: Shape Area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Activity 2: Employee Payment
class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate

class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary


# ==========================================
# TESTING ALL OUTPUTS
# ==========================================

if __name__ == "__main__":

    print("\n--- INHERITANCE OUTPUT ---")
    Dog().speak()
    Cat().speak()

    car = Car("Toyota", 5, 4)
    car.drive()
    car.drive()

    print("\n--- ENCAPSULATION OUTPUT ---")
    account = BankAccount()
    account.deposit(1000)
    account.withdraw(200)
    print("Balance:", account.get_balance())

    person = Person(20)
    print("Age:", person.age)
    try:
        person.age = -5
    except ValueError as e:
        print("Error:", e)

    print("\n--- POLYMORPHISM OUTPUT ---")
    InkPrinter().print_document()
    LaserPrinter().print_document()

    bird = Bird()
    robot = Robot()
    make_it_speak(bird)
    make_it_speak(robot)

    try:
        make_it_speak(123)
    except Exception as e:
        print("Error:", e)

    print("\n--- ABSTRACTION OUTPUT ---")
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print("Circle area:", circle.area())
    print("Rectangle area:", rectangle.area())

    hourly = HourlyEmployee(40, 150)
    salaried = SalariedEmployee(30000)
    print("Hourly Pay:", hourly.calculate_pay())
    print("Salaried Pay:", salaried.calculate_pay())
