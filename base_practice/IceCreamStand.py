from restaurant import *
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['apple','banana']
	def IceCream_flavors(self):
		print('you can choose the flavors in it:')
		for jk in self.flavors:
			print(jk)
xiaokeai=IceCreamStand('xiaokeai','chuancai')
xiaokeai.IceCream_flavors()
