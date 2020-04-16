"""
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
* Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
* Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
* Print a second set of invitation messages, one for each person who is still
in your list.
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