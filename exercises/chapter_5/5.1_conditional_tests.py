"""
Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. 
Your code should look something like this:
------------
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
------------
* Look closely at your results, and make sure you understand why each
line evaluates to True or False.
* Create at least ten tests. Have at least five tests evaluate 
to True and another five tests evaluate to False.
"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
car = "audi"
car2 = "BMW"
print(f"cars are {cars}")
print(f"car is {car}")
print(f"car2 is {car2}")
print()

print("Is car == 'audi'? I predict True.")
print(car == 'audi')
print("Is car == 'bmw'? I predict False.")
print(car == 'bmw')
print()

print("Is car != 'audi'? I predict False.")
print(car != 'audi')
print("Is car != 'bmw'? I predict True.")
print(car != 'bmw')
print()

print("'bmw' in cars? I predict True.")
print("bmw" in cars)
print("'bmw' not in cars? I predict False.")
print("bmw" not in cars)
print()

print("len(cars) > 3? I predict True.")
print(len(cars) > 3)
print("len(cars) <= 3? I predict False.")
print(len(cars) <= 3)
print("len(cars) >= 3 + 1? I predict True.")
print(len(cars) >= 3 + 1)
print()

print("cars[3] == 'subaru'? I predict False.")
print(cars[3] == 'subaru')
print()

"""
You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more 
tests and add them to conditional_tests.py. Have at least one 
True and one False result for each of the following:
* Tests for equality and inequality with strings
* Tests using the lower() method
* Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
* Tests using the and keyword and the or keyword
* Test whether an item is in a list
* Test whether an item is not in a list
"""

print("car2.lower() in cars? I predict True.")
print(car2.lower() in cars)
print()

print("len(cars[0]) < 4? I predict False.")
print(len(cars[0]) < 4)
print()

print("'audi' in cars and car2 == 'subaru'? I predict False")
print('audi' in cars and car2 == 'subaru')
print("'audi' in cars or car2 == 'toyota'? I predict True.")
print('audi' in cars or car2 == 'toyota')
print()

print("'volvo' not in cars? I predict True.")
print('volvo' not in cars)
