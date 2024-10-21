from Car import Car
"""
Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
Then print out the current speed of the car. 
Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
The travelled distance does not have to be updated yet.
"""
car1 = Car("ABC-123",142)
print(f"""
Registration number:{car1.registration_num},
Maximum speed:{car1.maximum_speed},
Current speed:{car1.current_speed},
Travelled distance:{car1.travelled_distance}
""")
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Current speed:{car1.current_speed} km/h")

car1.accelerate(-200)
print(f"Current speed:{car1.current_speed} km/h")