"""
Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.
"""
names = ["vlad", "margo", "yulia"]
message1 = f"Hello, {names[0].title()}!"
message2 = f"Hello, {names[1].title()}!"
message3 = f"Hello, {names[2].title()}!"

print(message1)
print(message2)
print(message3)