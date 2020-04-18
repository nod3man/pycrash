# It is possible to create almost any set of numbers with range.

# Calculating squares for integers from 1 to 10.
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print()

# More concise notation
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print()

# Use list comprehention
squares = [value ** 2 for value in range(1, 11)]
print(squares)