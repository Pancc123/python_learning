# -*- coding:utf-8 -*-

# 装饰器测试

def test_1(fun):
    def wrapper(*args, **kwargs):
        try:
            print("ok1")
            fun(*args, **kwargs)
            print("ok3")  # 在f执行后
        except Exception as e:
            print(e)
    # print("ok") 不在内嵌函数内先执行
    print("ok4")
    return wrapper

@test_1
def test_2(var):
    print("ok")
    print(var)




if __name__=='__main__':
    test_2("good")