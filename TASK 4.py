from Car import Car
import random
from tabulate import tabulate

# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on.
# Now the race begins. One per every hour of the race, the following operations are performed:
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accelerate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.

cars = ["AC-1", "AC-2", "AC-3", "AC-4", "AC-5", "AC-6", "AC-7", "AC-8", "AC-9", "AC-10"]
car1 = Car(cars[0],random.randint(100,200))
car2 = Car(cars[1],random.randint(100,200))
car3 = Car(cars[2],random.randint(100,200))
car4 = Car(cars[3],random.randint(100,200))
car5 = Car(cars[4],random.randint(100,200))
car6 = Car(cars[5],random.randint(100,200))
car7 = Car(cars[6],random.randint(100,200))
car8 = Car(cars[7],random.randint(100,200))
car9 = Car(cars[8],random.randint(100,200))
car10 = Car(cars[9],random.randint(100,200))

car_data1 =[
    [1,cars[0],car1.maximum_speed,0,0],
    [2,cars[1],car2.maximum_speed,0,0],
    [3,cars[2],car3.maximum_speed,0,0],
    [4,cars[3],car4.maximum_speed,0,0],
    [5,cars[4],car5.maximum_speed,0,0],
    [6,cars[5],car6.maximum_speed,0,0],
    [7,cars[6],car7.maximum_speed,0,0],
    [8,cars[7],car8.maximum_speed,0,0],
    [9,cars[8],car9.maximum_speed,0,0],
    [10,cars[9],car10.maximum_speed,0,0]
]
headers = ["number","Registration_number","Maximum_speed(km/h)","Current_speed(km/h)","Travelled_distance(km)"]
#print(tabulate(car_data1, headers=headers, tablefmt="grid")

car1.accelerate(random.randint(-10,15))
car1.drive(1)
car2.accelerate(random.randint(-10,15))
car2.drive(1)
car3.accelerate(random.randint(-10,15))
car3.drive(1)
car4.accelerate(random.randint(-10,15))
car4.drive(1)
car5.accelerate(random.randint(-10,15))
car5.drive(1)
car6.accelerate(random.randint(-10,15))
car6.drive(1)
car7.accelerate(random.randint(-10,15))
car7.drive(1)
car8.accelerate(random.randint(-10,15))
car8.drive(1)
car9.accelerate(random.randint(-10,15))
car9.drive(1)
car10.accelerate(random.randint(-10,15))
car10.drive(1)

car_data2 =[
    [1,cars[0],car1.maximum_speed,car1.current_speed,car1.travelled_distance],
    [2,cars[1],car2.maximum_speed,car2.current_speed,car2.travelled_distance],
    [3,cars[2],car3.maximum_speed,car3.current_speed,car3.travelled_distance],
    [4,cars[3],car4.maximum_speed,car4.current_speed,car4.travelled_distance],
    [5,cars[4],car5.maximum_speed,car5.current_speed,car5.travelled_distance],
    [6,cars[5],car6.maximum_speed,car6.current_speed,car6.travelled_distance],
    [7,cars[6],car2.maximum_speed,car7.current_speed,car7.travelled_distance],
    [8,cars[7],car3.maximum_speed,car8.current_speed,car8.travelled_distance],
    [9,cars[8],car4.maximum_speed,car9.current_speed,car9.travelled_distance],
    [10,cars[9],car5.maximum_speed,car10.current_speed,car10.travelled_distance],
]
headers = ["number","Registration_number","Maximum_speed(km/h)","Current_speed(km/h)","Travelled_distance(km)"]
print(tabulate(car_data2, headers=headers, tablefmt="grid"))