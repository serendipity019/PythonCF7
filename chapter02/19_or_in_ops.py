choice = 'q'

# Java approach
if choice == 'q' or choice == 'Q':
    print("Quit")
else:
    print("Continue")    


# Pythonial approach
if choice.upper() == 'Q':
    print("Quit")
else:
    print("Continue")   

# More Pythonial

if choice in ('q', 'Q'):
    print("Quit")
else:
    print("Continue")       