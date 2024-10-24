from Car import Car
import random
from tabulate import tabulate

# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.


cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100,200)))

distance_max = 0
while distance_max <10000:
    for car in cars:
        car.accelerate((random.randint(-15,10)))
        car.drive(1.)
        distance_max = max(car.travelled_distance, distance_max)

#START
car_data1 = []
for car in cars:
    car_data1.append([car.registration_number,car.maximum_speed])

print("THE LIST OF CAR:")
headers = ["Registration_number", "Maximum_speed(km/h)"]
print(tabulate(car_data1, headers=headers, tablefmt="grid", ))

#RESULT
car_data2 = []
for car in cars:
    car_data2.append([car.registration_number,car.maximum_speed,car.travelled_distance])
print("THE FINAL RESULTS:")
headers = ["Registration_number", "Maximum_speed(km/h)", "Travelled_distance(km)"]
print(tabulate(car_data2, headers=headers, tablefmt="grid", ))

