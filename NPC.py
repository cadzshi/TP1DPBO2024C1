#import
from Character import Character

#declare
class NPC(Character):
    #atribut private
    __tipe = ""

    #constructor
    def __init__(self, name = "", gender = "", atk = "", hp = "", role = "", item ="", tipe = ""):
        Character.__init__(self, name, gender, atk, hp, role, item)
        self.__tipe = tipe

    #setter
    def set_tipe(self, tipe):
        self.__tipe = tipe

    #getter
    def get_tipe(self):
        return self.__tipe
    
    
        