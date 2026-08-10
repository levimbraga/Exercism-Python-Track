class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        age = self.seconds / 31_557_600
        return round(age, 2)

    def on_mercury(self):
        age = self.seconds / 31_557_600
        age = age / 0.2408467
        return round(age, 2)
    
    def on_venus(self):
        age = self.seconds / 31_557_600
        age = age / 0.61519726
        return round(age, 2)
    
    def on_mars(self):
        age = self.seconds / 31_557_600
        age = age / 1.8808158
        return round(age, 2)
    
    def on_jupiter(self):
        age = self.seconds / 31_557_600
        age = age / 11.862615
        return round(age, 2)
    
    def on_saturn(self):
        age = self.seconds / 31_557_600
        age = age / 29.447498
        return round(age, 2)
    
    def on_uranus(self):
        age = self.seconds / 31_557_600
        age = age / 84.016846
        return round(age, 2)
    
    def on_neptune(self):
        age = self.seconds / 31_557_600
        age = age / 164.79132
        return round(age, 2)
    
