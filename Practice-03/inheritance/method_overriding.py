#1
class Animal:
    def make_sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    def make_sound(self):  # Overriding
        print("Bark! Bark!")
class Cat(Animal):
    def make_sound(self):  # Overriding
        print("Meow!")

#2
class Employee:
    def get_bonus(self, salary):
        return salary * 0.10  # Standard 10% bonus
class Developer(Employee):
    def get_bonus(self, salary):
        return salary * 0.15  # Developers get 15%
class Manager(Employee):
    def get_bonus(self, salary):
        return salary * 0.25  # Managers get 25%
    
#3
class BankAccount:
    def withdraw(self, amount):
        print(f"Withdrawing ${amount} from your account.")
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal limit exceeded for Savings Account!")
        else:
            super().withdraw(amount) # Calling the parent method

#4 
class Vehicle:
    def move(self):
        print("The vehicle is moving")
class Plane(Vehicle):
    def move(self):
        print("The plane is flying through the clouds")
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road")

my_dog = Dog()
my_cat = Cat()

my_dog.make_sound() 
my_cat.make_sound() 

my_car = Car()
my_car.move()     