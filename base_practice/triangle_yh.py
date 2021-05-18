# -*- coding=utf-8 -*
# @Time :  2021-4-21 16:42
# @Author : ChengCheng Pan
# 杨辉三角

def test():
    list1 = [1]
    while len(list1) < 10:
        yield list1
        if len(list1)==1:
            list1.append(1)
        else:
            list2 = list()
            for i in range(len(list1)-1):
                list2.append(list1[i] + list1[i + 1])
            list2.insert(0, 1)
            list2.append(1)
            list1 = list2
    return list1

t=test()
print(type(t))
for i in t:
    print(i)