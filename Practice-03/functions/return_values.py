#1 Returning a simple sum
def add_numbers(a, b):
    # The 'return' statement sends the result back to the caller
    return a + b

result = add_numbers(10, 5)
print(result)  # Output: 15

#2 Checking if a student is an adult
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
# Since Dias is 18, this will return True
print(is_adult(18))  # Output: True

#3 Returning multiple statistics at once
def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total, count  # Returns a tuple

s_total, s_count = get_stats([10, 20, 30])
print(f"Total: {s_total}, Count: {s_count}")

#4 Calculating area with a check
def calculate_area(radius):
    if radius < 0:
        return "Invalid radius" # Exit early if value is negative
    return 3.14 * (radius ** 2)
print(calculate_area(-5)) # Output: Invalid radius

#5 Returning a list of squared numbers
def square_list(items):
    new_list = []
    for i in items:
        new_list.append(i ** 2)
    return new_list
print(square_list([2, 3, 4]))  # Output: [4, 9, 16]