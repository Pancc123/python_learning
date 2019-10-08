class Dog:  # """ 一次模拟小狗的简单尝试"""
    def __init__(self, name, age): # 初始化属性name和age
        self.name=name
        self.age=age

    def sit(self): # """模拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self): # ""模拟小狗被命令打滚"""
        print(self.name.title() + ' rolled over!')


if __name__ =="__main__":
    my_dog = Dog('mike',6)
    print("My dog's name is "+my_dog.name.title()+'.')
    print("My dog's old is  "+str(my_dog.age)+'.')
    my_dog.sit()
    my_dog.roll_over()
