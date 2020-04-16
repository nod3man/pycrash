"""
You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
* Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
* Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
* Print a message to each of the two people still on your list, letting them
know they’re still invited.
* Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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

print(f"\nSadly but new table won't arrive in time, so I can dinner only with two friends.")
popped_friend = friends.pop(0)
print(f"Hello, {popped_friend.title()}. I can't invite you to the dinner.")
popped_friend = friends.pop(2)
print(f"Hello, {popped_friend.title()}. I can't invite you to the dinner.")
popped_friend = friends.pop(-1)
print(f"Hello, {popped_friend.title()}. I can't invite you to the dinner.")
popped_friend = friends.pop(1)
print(f"Hello, {popped_friend.title()}. I can't invite you to the dinner.")

print(f"\nHello, {friends[0].title()}. You're still invited to the dinner.")
print(f"Hello, {friends[1].title()}. You're still invited to the dinner.")

del friends[1]
del friends[0]
print(friends)