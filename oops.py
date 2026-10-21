# Variables and basic types/practice program
name = "Alice"          # String (str)
age = 25                # Integer (int)
height = 5.6            # Float (float)
is_student = True       # Boolean (bool)

# Conditional statements (adult or minor)
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1


#creating function
def calculate_area(length, width):
    return length * width

# Calling the function
area = calculate_area(5, 3)
print(f"Area: {area}")


#creating class and object.
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name       # Instance variable
        self.breed = breed     # Instance variable

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instantiation)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")



#inheritance

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using the child class
my_cat = Cat("Whiskers")
print(my_cat.speak())  # Output: Whiskers says Meow!

print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.breed)   # Output: German Shepherd


#encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Getter method to safely access private data
    def get_balance(self):
        return self.__balance

    # Setter method to modify private data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive!")

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)    # Error: 'BankAccount' object has no attribute '__balance'


#polymorphism
class Duck:
    def make_sound(self):
        return "Quack"

class Person:
    def make_sound(self):
        return "Hello"

def animal_sound(creature):
    print(creature.make_sound())

# Both objects have a make_sound method
animal_sound(Duck())    # Output: Quack
animal_sound(Person())  # Output: Hello



print("Thank You For Recall")

