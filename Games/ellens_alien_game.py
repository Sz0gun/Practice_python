class Alien:
    total_aliens_created = 0

    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alieve(self):
        return self.health > 0
    
    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def new_aliens_collection(positions):
        """Function taking a list of position tuples, creating one Alien instanse per position."""
        return [Alien(x, y) for x, y in positions]