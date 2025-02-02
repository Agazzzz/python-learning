class Car:
    #Properti
    type = "Fiat"
    model = "500"
    color = "white"

    #Method
    def start(self):
        print("Engine started")
    def drive(self):
        print("Drive the car")
    def brake(self):
        print("Apply the brake")
    def stop(self):
        print("Engine stopped")

my_car = Car()
my_car.brake()