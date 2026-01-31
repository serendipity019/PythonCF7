name = "Bob"

print("--- or ---")

valid_user = None or "User"
print("Hello,", valid_user)

print("-" * 20)

# short-circuit evaluation with or 
#Returns the first truthy value or the last value if none are truthy
valid_user = name or "User" # since name is truthy, it will be returned
print("Hello,", valid_user)


valid_user = "User" or name # since "User" is truthy, it will be returned
print("Hello,", valid_user)

# short-circuit evaluation with and
print("--- and ---")

email = "example@email.com"
valid_email = email != "" and email
print("Valid email:", valid_email) # Return True, since both are truthy and the email != "" is True. 

#valid_email = email and (email != "") and "Panos"  # all are truthy, so the last one is returned
#print("Valid email:", valid_email)

if valid_email:
    print(f"Hello, {valid_user}. Your email is {valid_email}")
else:
    print(f"Hello, {valid_user}. You have not provided a valid email.")    