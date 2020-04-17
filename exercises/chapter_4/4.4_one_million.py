"""
Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.)
"""
million = list(range(1, 1_000_001))
for x in million:
    print(x)
