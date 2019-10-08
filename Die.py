from random import randint

class die():
	def __init__(self):
		self.sides=6
	def roll_die(self):
		digtal=randint(1,self.sides)
		print(digtal)
		
get=die()
"""for i  in range(1,10):
	get.roll_die()
"""
i=1
while i<=10:
	get.roll_die()
	i+=1
