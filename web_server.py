#从wsgiref 模块导入
from wsgiref.simple_server import make_server
#导入我们自己编写的application 函数
from hello import application
#创建一个服务器IP地址为空,端口是8999，处理函数是appliction:
httpd=make_server('', 8999, application)
print('Serving HTTP on port 8999...')
#开始我们的监听
httpd.serve_forever()

