# To check whether item is not in the list, use keywords 'not' and 'in'.
banned_users = ['andrew', 'carolina', 'david']
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
