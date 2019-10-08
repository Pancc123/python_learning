from User import User

class Privileges():
	#privileges=['can add post','can delete post','can ban post']
	def __init__(self,privileges=['can add post','can delete post','can ban post']):
		self.privileges=privileges
	def show_privileges(self):
		for privileges in self.privileges:
			print(privileges)


class Admin(User):
	def __init__(self,first_name,last_name,age,location):
		super().__init__(first_name,last_name,age,location)
		self.privileges=Privileges()


pcc=Admin('pan','chengcheng',22,'zj')
pcc.privileges.__init__(['can get'])
pcc.privileges.show_privileges()
