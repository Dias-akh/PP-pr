#1 The function will receive a tuple of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#2 Accessing individual arguments from *args:
def my_function(*args): # Arbitrary argument-when we don't know how many arguments we might expect
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function("Dias", "Daulet", "Zhandos")

#3 Regular parameters with *args
def my_function(greeting, *names): # greeting will receive "Hello"
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")

#4 A function that calculates the sum of any number of values
def my_function(*numbers): #creates a tuple 
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#5 Accessing values from **kwargs:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")