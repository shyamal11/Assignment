class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, other):
        total_minutes = (self.hours * 60 + self.minutes) + (other.hours * 60 + other.minutes)
        return Time(total_minutes // 60, total_minutes % 60)
    
    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")
    
    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minutes")


time1 = Time(2, 50)
time2 = Time(1, 20)

added_time = time1.addTime(time2)
added_time.displayTime()
added_time.displayMinutes()
