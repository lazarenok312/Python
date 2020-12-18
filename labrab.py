from abc import ABC, abstractmethod
import math
import random

class Character(ABC):
	def __init__(self, name, level,,max_hp,hp,armour_class,initiative)
	self.name = name
	self.level = level #уровень
	strength = "8" #сила
	dexterity = "8" #ловкость
	constitution = "8" #телосложение
	intelligence = "8" #интелект
	wisdom = "8" #мудрость 
	charisma = "8" #харизма
	self.max_hp = max_hp 
	self.hp = hp
	self.armour_class = armour_class
	self.initiative = initiative

	def attack(self):
		pass

	def save_throw(self, attribute):
		pass

	@abstractmethod
	def perk(self):
		pass

hero_name = input("Введите имя героя")
hero_lvl = input("Введите уровень героя")
c = Character()
c.name = hero_name()
c.level = hero_lvl()


class Hero(Character):
	@abstractmethod
	def perk(self):
		
class Dragon(Character):
	@abstractmethod
	def perk(self):

d6 = random.uniform(1, 12)
d8 = random.uniform(1, 16)
d20 = random.uniform(1, 20)
d10 = math.floor(d20)

max_hp = 10 + constitution + 1d10 * level
hp = max_hp
armour_class = 15 + dexterity
initiative = 1d20 + dexterity