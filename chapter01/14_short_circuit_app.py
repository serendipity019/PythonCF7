username = input("Please enter your username: ")

email = input("Please enter your email address: ")

Valid_user = username or "User"

'''
if email: 
    print(f"Hello {Valid_user}, your email address is {email}.")
else:
    print(f"Hello {Valid_user}, you did not provide an email address.")    
'''

print(f"Hello {Valid_user}, " + ((email and f"your email is {email}.") or "you did not provide an email address."))