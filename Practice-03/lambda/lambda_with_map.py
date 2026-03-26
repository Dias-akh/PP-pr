#1 Double all numbers in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2 Converting a list of strings to uppercase
names = ["dias", "kbtu", "python"]
uppercase_names = list(map(lambda name: name.upper(), names))
print(uppercase_names) 

#3 Squaring each number in a list
numbers = [2, 4, 6, 8]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#4 Adding corresponding elements of two lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
summed_lists = list(map(lambda x, y: x + y, list1, list2))
print(summed_lists)

#5 Getting the length of each word in a list
words = ["apple", "banana", "cherry"]
word_lengths = list(map(lambda word: len(word), words))
print(word_lengths)



