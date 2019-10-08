from User import *
class Admin(User):
	def __init__(self,first_name,last_name,age,location):
		super().__init__(first_name,last_name,age,location)
		self.privileges=['can add post','can delete post','can ban post']
	def show_privileges(self):
		for privileges in self.privileges:
			print(self.first_name.title()+self. last_name.title()+'\t'+privileges+'.')

pcc=Admin('pan','chengcheng',22,'zj')
pcc.show_privileges()
