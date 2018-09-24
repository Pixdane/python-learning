p = -5
def quadratic(a,b,c):
    import math
    if not isinstance(a or b or c,(int,float)):
        raise TypeError('bad operand type')
    if a == 0:
        raise TypeError('a can\'t be zero!')
    delta = b**2-4*a*c
    if delta < 0:
        x1 = None
        x2 = None
        result = '无实根'
    else:
        x1 = ((-b+math.sqrt(delta))/(2*a))
        x2 = ((-b-math.sqrt(delta))/(2*a))
        result = None
    return x1,x2,result
qa = 'x^2'
while p < 0:
    a = float(input('请输入a的值：'))
    b = float(input('请输入b的值：'))
    c = float(input('请输入c的值：'))
    x1,x2,result = quadratic(a,b,c)
    print('y=+(',a,')',qa,'+(',b,')x+(',c,')')
    if result == None:
        print('x1=',x1,'\nx2=',x2)
    else:
        print(result)
    while p < 0:
        c = input('是否继续计算(y/n)：')
        if c == 'y':
            break
        elif c == 'n':
            break
        else:
            print('请输入y/n')
            pass
    if c == 'y':
        pass
    else:
        break