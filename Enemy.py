#import
from NPC import NPC

#declare
class Enemy(NPC):
    #constructor
    def __init__(self, name = "", gender = "", atk = "", hp = "", role = "", item ="", tipe = ""):
        NPC.__init__(self, name, gender, atk, hp, role, item, tipe)

    def talking(self):
        print(f"{super().get_name()} is talking")
    
    def reward(self):
        print(f"{super().get_name()} memberikan {self.__item} x20")

   