from collections import deque

def display_garage(garage: deque) -> None:
    if garage:
        for position, car in enumerate(garage, 1):
            print(f"{position}. {car}")
    else: 
        print("The garage is empty")

def add_car_to_garage(garage: deque, max_capacity: int) -> None:
    if len(garage) < max_capacity:
        car_name = input("Enter the name or ID of the car: ")
        garage.append(car_name)
        print(f"{car_name} has entered in the garage.")
    else:
        print("The garage is full. Cannot add more cars.")

def remove_car_from_garage(garage: deque):
    if garage:
        car_left = garage.popleft
        print(f"{car_left} has left from the garage.")
    else:
        print("Garage is empty. No cars to remove.")

def main():
   # ToDo: menu list that add and remove cars from the garage.
   # ToDo: more complicate garage. To can remove any car from garage not only FIFO. (hint! Dictionary car_name : position) 
   pass

if __name__ == "__main__":
    main()