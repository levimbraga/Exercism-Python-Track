class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = (minute + (hour * 60)) % 1440
        self.hour = self.total_minutes // 60
        self.minute = self.total_minutes % 60


    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other): 
        return self.total_minutes == other.total_minutes   

    def __add__(self, minutes):
        new_clock = self.total_minutes + minutes
        return Clock(0, new_clock)

    def __sub__(self, minutes):
        new_clock = self.total_minutes - minutes
        return Clock(0, new_clock)