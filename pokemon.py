class Pokemon:
    def __init__(self, id, name, weight, height, trainer):
        self.__id = id
        self.name = name
        self.weight = weight
        self.height = height
        
        from trainer import Trainer
        if not isinstance(trainer, Trainer):
            raise TypeError("trainer debe ser una instancia de la clase Trainer")
        
        self.trainer = trainer

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def __str__(self):
        return self.name

    def attack(self):
        return f"{self.name} lanzó un ataque!"
