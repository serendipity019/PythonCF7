my_list = [ 1, 2, "Hello", [3, 4, 5]]

print("At the start")
for item in my_list:
    print(f"{item} : {id(item)}")

new_list = my_list * 2
print("Duplicated list:", new_list)    

new_list[0] = 100
print("Modified list:", new_list)  

new_list[3][0] = 300
print("Duplicated list (2):", new_list) # We expect to take this: [1, 2, 'Hello', [300, 4, 5], 1, 2, 'Hello', [3, 4, 5]] but change and the duplicate list inside. 

print("New print")
for item in new_list:
    print(f"{item} : {id(item)}")