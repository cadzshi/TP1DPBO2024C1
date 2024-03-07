#import
from Character import Character

#declare
class Player(Character):
    #atribut private
    __level = ""

    #construtor
    def __init__(self, name = "", gender = "", atk = "", hp = "", role = "", item ="", level = ""):
        Character.__init__(self, name, gender, atk, hp, role, item)
        self.__level = level
    
    #setter
    def set_level(self, level):
        self.__level = level
    
    #getter
    def get_level(self):
        return self.__level
    
    def mission(self):
        print(f"{super().get_name()} is giving the first mission")
    
    def add_item(self):
        print(f"{super().get_name()} add new {self.__item}")