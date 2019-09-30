
#!/usr/sbin/python3
error_num=3
username=input('输入用户名：')
if username=="pcc":
	while True:
		passwd=input('输入密码：')
		if passwd=="123456":
			print('login sucessfully')
		else:
			print('密码输入错误')
			error_num=error_num-1
			if error_num==0:
				exit()
			else:
				continue
else:
	print('用户名输入错误')

