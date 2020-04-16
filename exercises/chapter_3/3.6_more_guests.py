"""
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
* Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
* Use insert() to add one new guest to the beginning of your list.
* Use insert() to add one new guest to the middle of your list.
* Use append() to add one new guest to the end of your list.
* Print a new set of invitation messages, one for each person in your list.
"""
friends = ["vlad", "margo", "yulia"]
print(f"Hello, {friends[0].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[1].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[2].title()}. Would you like to dinner with me?")

cant_dinner = friends.pop(1)
print(f"\n{cant_dinner.title()} can't dinner with me. I will invite someone else.")

friends = ["vlad", "ilga", "yulia"]
print(f"Hello, {friends[0].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[1].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[2].title()}. Would you like to dinner with me?")

print(f"\nI've found a bigger dinner table. We can invite more guests!")

friends.insert(0, "ivan")
friends.insert(2, "leonid")
friends.append("oleg")
print(f"Hello, {friends[0].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[1].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[2].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[3].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[4].title()}. Would you like to dinner with me?")
print(f"Hello, {friends[5].title()}. Would you like to dinner with me?")