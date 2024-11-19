from pokemon import Pokemon

class ElectricPokemon(Pokemon):
    def __init__(self, id, name, weight, height, trainer):
        super().__init__(id, name, weight, height, trainer)
    
    def attack(self):
        return f"{self.name} lanzó un ataque eléctrico!"

