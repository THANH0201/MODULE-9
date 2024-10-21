
#Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
#Add a class initializer that sets the first two of the properties based on parameter values.
#The current speed and travelled distance of a new car must be automatically set to zero.

#class Car:
#    def __init__(self,reg_num, max_speed, cur_speed = 0, trav_dist = 0):
#        self.registration_num = reg_num
#        self.maximum_speed = max_speed
#        self.current_speed = cur_speed
#        self.travelled_distance = trav_dist

class Car:
    def __init__(self,reg_num, max_speed):
        self.registration_num = reg_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

#Extend the program by adding an accelerate method into the new class.
#The method should receive the change of speed (km/h) as a parameter.
#If the change is negative, the car reduces speed.
#The method must change the value of the speed property of the object.
#The speed of the car must stay below the set maximum and cannot be less than zero.

    def accelerate(self,speed_change):
        self.current_speed = speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
#Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.
    def drive(self, time):
        self.travelled_distance += (self.current_speed * time) #(d=v.t)


