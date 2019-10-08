def get_sun_numbers():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, '等于', x, '*', n//x)
                break
            else:  # 循环中没有找到元素
                print(n, ' 是质数')


def get_user_list():
    current_users = ['andy', 'wang', 'chen', 'lin', 'xia']
    new_users = ['andy', 'wang', 'chen', 'lin', 'xia', 'jiang']
    for users in new_users:
        if users.lower() in current_users:
            print('Please enter other user_name')
        else:
            print('this user_name is not used')