from trainer import Trainer
from pokemon import Pokemon
from electric_pokemon import ElectricPokemon
from water_pokemon import WaterPokemon
from fire_pokemon import FirePokemon

trainer = Trainer(1, "Ash", "Ketchum", 10, 5)

pikachu = ElectricPokemon(25, "Pikachu", 6.0, 0.4, trainer)
squirtle = WaterPokemon(7, "Squirtle", 9.0, 0.5, trainer)
charizard = FirePokemon(6, "Charizard", 90.5, 1.7, trainer)

trainer.add_pokemon(pikachu)
trainer.add_pokemon(squirtle)
trainer.add_pokemon(charizard)

print(f"Entrenador: {trainer}")
print(f"Pokedex de {trainer}:")
for pokemon in trainer.pokedex:
    print(f"- {pokemon.name}: {pokemon.attack()}")
