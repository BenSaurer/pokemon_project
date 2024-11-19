from pokemon import Pokemon

class Trainer:
    def __init__(self, id, first_name, last_name, age, level):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level
        self.pokedex = []  
    
    def add_pokemon(self, pokemon):
        if isinstance(pokemon, Pokemon):
            self.pokedex.append(pokemon)
        else:
            raise TypeError("Solo se pueden agregar instancias de Pokémon.")
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

