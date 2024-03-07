#declare
class Character:
    #atribut private
    __name =""
    __gender = ""
    __atk = ""
    __hp = ""
    __role = ""
    __item = ""

    #constructor
    def __init__(self, name = "", gender = "", atk = "", hp = "", role = "", item =""):
        self.__name = name
        self.__gender = gender
        self.__atk = atk
        self.__hp = hp
        self.__role = role
        self.__item = item
        
    #setter
    def set_name(self, name):
        self.__name = name
    def set_gender(self, gender):
        self.__gender = gender
    def set_atk(self, atk):
        self.__atk = atk
    def set_hp(self, hp):
        self.__hp = hp
    def set_role(self, role):
        self.__role = role
    def set_item(self, item):
        self.__item = item

    #getter
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def get_atk(self):
        return self.__atk
    def get_hp(self):
        return self.__hp
    def get_role(self):
        return self.__role
    def get_item(self):
        return self.__item
    
    def attacking(self):
        print(self.__name, "is Attacking")
    def skill(self):
        print(self.__name, "is Using Skill")
    def upgrade(self):
        print(self.__name, "is Upgrading")



