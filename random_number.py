import random
tmp=''# 最后生成的随机码
for i in range(4):
    n=random.randrange(0,2) # 生成随机数1或0，用来判断下面，是生成随机数字，还是字母
    if n==0:
        num = random.randrange(65, 91) # 为0时候，生成大写字母
        tmp+=chr(num)
    else:
        k=random.randrange(0,10)# 为1时候，生成数字
        tmp+=str(k)
print(tmp)# 这里运行的时候每次生成的4为随机码都不同
