cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

""" 
Equality operator returns True if left and right match, False otherwise. 
"""

car = "bmw"
car == "bmw"
# True

car = "audi"
car == "bmw"
# False

# Equality tests are case sensitive.
car = "Audi"
car == "audi"
# False

car = "Audi"
car == car.lower()
# True
