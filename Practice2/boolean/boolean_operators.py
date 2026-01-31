#1
print(bool("Hello"))
print(bool(15))
#2
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#3 The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#4 The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#5 Functions
def myFunction() :
  return True

print(myFunction())
