import random
import string

class Robot:
    used_names = []
    def __init__(self):
        self.name = self.create_name()

    def create_name(self):
        while True:
            letter1 = random.choice(string.ascii_uppercase)
            letter2 = random.choice(string.ascii_uppercase)
            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
            number3 = random.randint(0, 9)
            name = f'{letter1}{letter2}{number1}{number2}{number3}'
            if name in self.used_names:
                continue
            else:
                self.used_names.append(name)
                break
        return name

    def reset(self):
        self.name = self.create_name()