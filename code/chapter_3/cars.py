cars = ['bmw', 'audi', 'toyota', 'subaru']

# sort method sorts list permanently in alphabetical order
cars.sort()
print(cars)

# list sorted permanently in reversed order
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

# sorted function sorts list temporarily in alphabetical order
print(sorted(cars))

# list sorted temporarily in alphabetical order
print(sorted(cars, reverse=True))

# reverse method reverses order permanently
cars.reverse()
print(cars)

# len function determines lenght of the list
print(len(cars))
