#! -*- coding:utf-8 -*-

import re
test = '正则表达式1'
if re.match(r'正则表达式', test,re.S):
    print('ok')
else:
    print('failed')
