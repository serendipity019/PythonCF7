num = 10 # is primitive
my_dict = {"count": 0}

def main():
#   global num
   print(my_dict)
   my_dict["count"] += 1
   print(my_dict) # We see that the dict change
#   num += 100 # We will take error because the num is primitive and the value is in the stuck
   print(num) 
   print(num + 100) # This work because create a new value in the stuck 
   num = 20
   num += 100
   print(num) 

if __name__ == "__main__":
    main()