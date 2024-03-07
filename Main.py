from Character import Character
from Player import Player
from NPC import NPC
from Friend import Friend
from Enemy import Enemy



# Membuat data Player
player1 = Player("Nova", "Male", "10", "100", "DPS", "Sword", "5")
player2 = Player("Jane", "Female", "12", "120", "Healer", "Staff", "7")

# Membuat data Enemy
enemy1 = Enemy("Thor", "Male", "8", "80", "Enemy", "Hammer", "Human")
enemy2 = Enemy("Balmond", "Male", "15", "150", "Boss", "Axe", "Beast")

# Membuat data Friend
friend1 = Friend("Adryan", "Male", "8", "80", "Villager", "Food", "Human")
friend2 = Friend("Lyra", "Female", "10", "100", "Merchant", "Potion", "Human")

# Menjalankan method dari masing-masing objek
print("--- Players ---")
print("Player 1 :")
print(f"Name : {player1.get_name()} \nLevel : {player1.get_level()} \nATK : {player1.get_atk()} \nHP : {player1.get_hp()} \nRole : {player1.get_role()} \nItem : {player1.get_item()} \nGender : {player1.get_gender()}")
print()
print("Player 2 :")
print(f"Name : {player2.get_name()} \nLevel : {player2.get_level()} \nATK : {player2.get_atk()} \nHP : {player2.get_hp()} \nRole : {player2.get_role()} \nItem : {player2.get_item()} \nGender : {player2.get_gender()}")

print()
print("--- NPC ---")
print("Good NPC :")
print(f"Name : {friend1.get_name()} \nTipe : {friend1.get_tipe()} \nATK : {friend1.get_atk()} \nHP : {friend1.get_hp()} \nRole : {friend1.get_role()} \nItem : {friend1.get_item()} \nGender : {friend1.get_gender()}")
print()
print("Evil NPC :")
print(f"Name : {enemy1.get_name()} \nTipe : {enemy1.get_tipe()} \nATK : {enemy1.get_atk()} \nHP : {enemy1.get_hp()} \nRole : {enemy1.get_role()} \nItem : {enemy1.get_item()} \nGender : {enemy1.get_gender()}")

print()
print("--- Interactions ---")
friend1.give_mission()
friend2.attacking()
enemy1.talking()
