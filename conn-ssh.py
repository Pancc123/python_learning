import paramiko
from pymysql import connect, cursors

try:
	# 建立一个sshclient对象
	ssh = paramiko.SSHClient()
	# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# 调用connect方法连接服务器
	ssh.connect(hostname='192.168.10.101', port=22, username='root', password='rootelink')
	# 执行命令
	stdin, stdout, stderr = ssh.exec_command('ifconfig;batc get_all;')
	print('进入终端')

	# 结果放到stdout中，如果有错误将放到stderr中
	print(stdout.read().decode())
	# 关闭连接
	ssh.close()
except Exception as e:
	print(e)