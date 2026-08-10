"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate, health=3):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(alien_start_positions):
    aliens = []
    for alien in alien_start_positions:
        new_alien = Alien(alien[0], alien[1])
        aliens.append(new_alien)
    return aliens   


#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates


