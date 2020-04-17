""" 
Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once. 
"""
countries = ["poland", "spain", "equador", "bali", "egypt"]
print(countries)
print(countries[0])
print()

# adding items to the list
# add to the end of the list
countries.append("france")
# add to the n position of the list
countries.insert(2, "norway")
print(countries)
print()

# removing items
# remove item n
del countries[4]
# remove last item and extract value
popped_country = countries.pop()
# remove item n and extract value
popped_country_n = countries.pop(4)
# remove first matched item
countries.remove("spain")
print(popped_country)
print(popped_country_n)
print(countries)
print()

# sorting
# temporarily sort list - alphabeticaly
print(sorted(countries))
# temporarily sort list - reverse-alphabeticaly
print(sorted(countries, reverse=True))
print()

# reverse order of the list
countries.reverse()
print(countries)
print()

# sort list alphabetically
countries.sort()
print(countries)
# sort list reverse-alphabetically
countries.sort(reverse=True)
print(countries)

# print lenght of the list
print(len(countries))