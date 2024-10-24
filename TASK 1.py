from Car import Car
"""
Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
Finally, print out all the properties of the new car.
"""
car1 = Car("ABC-123",142)
print(f"""
Registration number:{car1.registration_number},
Maximum speed:{car1.maximum_speed},
Current speed:{car1.current_speed},
Travelled distance:{car1.travelled_distance}
""")




