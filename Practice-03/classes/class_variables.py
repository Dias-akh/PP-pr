#1 Change the age property
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Tobias", 25)
print(p1.age)
p1.age = 26
print(p1.age)

#2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Linus", 30)
del p1.age
print(p1.name) # This works
# print(p1.age) # This would cause an error

#3 class Person:
class Person:
  species = "Human" # Class property
  def __init__(self, name):
    self.name = name # Instance property
p1 = Person("Emil")
p2 = Person("Tobias")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#4 Change a class property
class Person:
  lastname = ""
  def __init__(self, name):
    self.name = name
p1 = Person("Linus")
p2 = Person("Emil")
Person.lastname = "Refsnes"
print(p1.lastname)
print(p2.lastname)

#5 Add a new property to an object
class Person:
  def __init__(self, name):
    self.name = name
p1 = Person("Tobias")
p1.age = 25
p1.city = "Oslo"
print(p1.name)
print(p1.age)
print(p1.city)