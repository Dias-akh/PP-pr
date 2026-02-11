#1
def my_function(name = "friend"): #default parameter value
  print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function() #uses "friend" as default
my_function("Linus")

#2 Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(name = "Buddy", animal = "dog") # The order does not matter

#3 Mixing positional and Keyword arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function("dog", name = "Buddy", age = 5)

#4 Dictionary as an argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#5 Returning the list
def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])