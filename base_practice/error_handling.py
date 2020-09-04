def division_test(divisor):
    try:
        print('try...')
        r = 10 / int(divisor)
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')
    return 1


divisors = ['10','a',10,0]
for i in divisors:
    result1 = division_test(i)


