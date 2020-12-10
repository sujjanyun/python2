# Small Exercise #2,3,4
numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6]

max_number = max(numbers)
print(max_number)

min_number = min(numbers)
print(min_number)

# list comprehension

even = [num for num in numbers if num % 2 == 0]
print(even)

# for loops

for num in numbers:
    if num % 2 == 0:
        print(num, end = " ")