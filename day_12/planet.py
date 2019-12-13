class Planet:
    def __init__(self, position):
        self.position: list = position
        self.velocity: list = [0, 0, 0]

    def get_potential_energy(self):
        return sum(map(lambda pos_value: abs(pos_value), self.position))

    def get_kinetic_energy(self):
        return sum(map(lambda pos_value: abs(pos_value), self.velocity))

    def get_total_energy(self):
        return self.get_kinetic_energy() * self.get_potential_energy()
