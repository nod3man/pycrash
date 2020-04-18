# To copy list use slice with [:] (=[0:-1])
# If no slice is used then second list will be the same list with different label
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print()

# Lists are not different
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)
