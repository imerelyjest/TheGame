#create weapons with the method
class weapon:
	def __init__(self, name, damage):
		self.name = name
		self.damage = damage
#create all character and npc types
class Character:
	def __init__(self, name, hp, attack, mod=0):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.mod = mod
		self.actions = ['Attack', 'Bag', 'Observe', 'Run']

	def choose_action(self):
		i = 1
		print("\nActions")
		for action in self.actions:
			print(str(i) + ":", action)
			i += 1

	def shortsword_attack(self):
		self.dmg = self.mod

	def get_hp(self):
		return self.hp

	def take_dmg(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

goblin = Character('Goblin', 10, 0)
shortsword = weapon('Shortsword', 5)
hero = Character('Greyland', 100, 1, shortsword.damage)

running = True
def battle(hero, goblin):
	while running:
		 hero.choose_action()
		 choice = input("Choose action: ")
		 index = int(choice) - 1

		 if index == 0:
		 	dmg = hero.shortsword_attack()
		 	goblin.take_dmg(dmg)
		 	print(hero.name.replace(" ", "") + " deals ", dmg, " to " , goblin.name.replace(" ", ""))
		 	if goblin.get_hp() == 0:
		 		print(goblin.name.replace(" ", "") + " has died.")
		 		del goblin

def main():
	battle(hero, goblin)

if __name__ == '__main__':
	main()