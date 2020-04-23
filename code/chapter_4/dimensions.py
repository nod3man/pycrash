# Tuples are immutable lists
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()

""" 
It is possible to define tuples without parentheses
dimensions = 300, 100
print(dimensions[0])
print(dimensions[1])
"""

# It is possible to loop through tuples
for dimension in dimensions:
    print(dimension)

# It is possible to create new tuple with the same name
print()
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print()

dimensions = (300, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)