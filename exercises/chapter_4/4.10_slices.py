"""
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
* Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
* Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
* Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.
"""
# 4.9_cube_comprehension.py
cubes = [x ** 3 for x in range(1, 11)]

for x in cubes:
    print(x)

print("The first three items in the list are:")
print(cubes[:3])
print("Four items from the middle of the list are:")
print(cubes[3:7])
print("The last three items in the list are:")
print(cubes[-3:])

