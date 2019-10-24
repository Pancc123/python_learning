banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
	print(user.title()+',you can post a respose if you with.')
	
fruit='apple'
print("is fruit=='orange'? I predict False.")
print(fruit=='orange')

print("\nIs fruit==apple'? I predict True.")
print(fruit=='apple')

alien=['green','red','yellow']
if 'green' in alien:
	print('Player win 5 point')
elif 'yellow' in alien:
	print('Player win 10 point')
else:
	print('Player win 15 point')