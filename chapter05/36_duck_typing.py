class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclass should implement this.")
    
class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bicycle(Vehicle):
    def drive(self):
        print("Riding a bicycle")

class Hoverboard:
    def drive(self):
        print("Hovering a hoverboard")        

class Boat(Vehicle):
    def sail(self):
        print("Sailing a boat")

# Polymorphic method
def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} can't drive")

def main():
    my_car = Car()
    my_bicycle = Bicycle()
    my_hoverboard = Hoverboard()
    my_boat = Boat()

    my_vehicles = [my_car, my_bicycle, my_hoverboard, my_boat]

    for vehicle in my_vehicles:
        drive_vehicle(vehicle)


if __name__ == "__main__":
    main()  
             