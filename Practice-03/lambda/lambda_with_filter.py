#1 Filter out even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2 Keeping only positive numbers from a list
numbers = [-10, 5, -2, 8, -1, 0, 15]
positive_numbers = list(filter(lambda x: x > 0, numbers))

print(positive_numbers)  # Output: [5, 8, 15]

#3 Filtering out short words (length less than or equal to 3)
words = ["hi", "python", "it", "code", "ai"]
long_words = list(filter(lambda word: len(word) > 3, words))

print(long_words)  # Output: ['python', 'code']

#4 Finding names that start with the letter 'D'
students = ["Dias", "Arman", "Dina", "Alibi"]
d_names = list(filter(lambda name: name.startswith("D"), students))

print(d_names)  # Output: ['Dias', 'Dina']

#5 Keeping only numbers that are greater than 50
grades = [20, 88, 45, 92, 70, 30]
high_grades = list(filter(lambda score: score > 50, grades))
print(high_grades)  # Output: [88, 92, 70]