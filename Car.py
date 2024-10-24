
class Car:
    def __init__(self,reg_num, max_speed):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Change speed
    def accelerate(self,speed_change):
        self.current_speed = speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

#time drive
    def drive(self, time):
        self.travelled_distance += round((self.current_speed * time)) #(d=v.t)



