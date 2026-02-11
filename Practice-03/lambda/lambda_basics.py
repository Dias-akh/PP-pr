# lambda arguments : expression
#1 Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#2 Multiply argument a with argument b and return the result
x = lambda a, b : a * b
print(x(5, 6))

#3 Summarize argument a, b, and c and return the result
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#4
x = lambda a, b, c : a/b + c
print(x(6, 5, 3))
