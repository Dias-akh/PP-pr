#1 Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2 Sort strings by length:
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#3 Sorted by absolute value
numbers = [-15, 2, -30, 10, -5]
# The lambda takes each 'x' and sorts based on abs(x)
sorted_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_abs)  # Output: [2, -5, 10, -15, -30]

#4 Sorting words based on their last letter
fruits = ["banana", "apple", "cherry"]
# lambda x: x[-1] takes the last character of each string
sorted_fruits = sorted(fruits, key=lambda x: x[-1])
print(sorted_fruits)  # Output: ['banana', 'apple', 'cherry'] 
# (sorted by 'a', 'e', 'y')

#5 Sorting dictionary keys by their values (prices)
prices = {'apple': 50, 'orange': 20, 'banana': 30}
# We sort the keys by looking up their values in the dictionary
sorted_by_price = sorted(prices, key=lambda x: prices[x])
print(sorted_by_price)  # Output: ['orange', 'banana', 'apple']