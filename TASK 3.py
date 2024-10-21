from Car import Car
#Method call car.drive(1.5) increases the travelled distance to 2090 km.


car1 = Car("ABC-123",142)
car1.accelerate(140)
car1.drive(1.5)
car1.accelerate(130)
car1.drive(1.5)
car1.accelerate(150)
car1.drive(1.5)
car1.accelerate(140)
car1.drive(1.5)
car1.accelerate(130)
car1.drive(1.5)
car1.accelerate(150)
car1.drive(1.5)
car1.accelerate(110)
car1.drive(1.5)
car1.accelerate(120)
car1.drive(1.5)
car1.accelerate(130)
car1.drive(1.5)
car1.accelerate(100)
car1.drive(1.5)
car1.accelerate(109.35)
car1.drive(1.5)

print(f"""
Registration number:{car1.registration_num},
Maximum speed:{car1.maximum_speed} km/h,
Current speed:{car1.current_speed} km/h,
Travelled distance:{int(car1.travelled_distance)} km
""")