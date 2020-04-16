motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Append method adds new item to the end of the list
motorcycles.append("kawasaki")
print(motorcycles)

# Insert method allows adding new items to any position of the list
motorcycles.insert(0, "honda")
print(motorcycles)

# Remove any item from the list using del statement
del motorcycles[0]
print(motorcycles)

# Remove last item from the list and extract it's value using pop method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Remove any item from the list and extract it's value using pop method
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

# Remove any item from the list using remove method
motorcycles.remove("suzuki")