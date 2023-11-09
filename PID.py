class PID:

    def __init__(self,
                 goal = 0,
                 kp = 0,
                 ki = 0,
                 kd = 0,
                 risingTime = 0,
                 maxOvershoot = 0,
                 unit =  "rad/s"
                 ):
        self.goal = goal
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.risingTime = risingTime
        self.maxOvershoot = maxOvershoot
        self.unit = unit
    
    def setGoal(self, goal):
        self.goal = goal

    def setKp(self, kp):
        self.kp = kp
    
    def setKi(self, ki):
        self.ki = ki
    
    def setKd(self, kd):
        self.kd = kd
    
    def setMaxOvershoot(self, maxOvershoot):
        self.maxOvershoot = maxOvershoot
    
    def setRisingTime(self, risingTime):
        self.risingTime = risingTime
    
    def setUnit(self, unit):
        self.unit = unit

print("test")