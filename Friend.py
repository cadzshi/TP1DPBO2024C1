#import
from NPC import NPC

#declare
class Friend(NPC):
    
    #constructor
    def __init__(self, name = "", gender = "", atk = "", hp = "", role = "", item ="", tipe = ""):
        NPC.__init__(self, name, gender, atk, hp, role, item, tipe)

    def give_mission(self):
        print(f"{super().get_name()} memberikan mission pertama")
    
    def sell_item(self):
        print(f"{super().get_name()} menjual {self.__item} ")

    def buy_item(self):
        print(f"{super().get_name()} membeli {self.__item} ")
