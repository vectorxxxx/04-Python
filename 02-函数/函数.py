def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    

def nop():
    pass

def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(x, n):
    s = 1
    while n>0:
        n -= 1
        s *= x
    return s


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n**2
    return sum


def mul(x, *y):
    if len(y) == 0:
        return x
    for i in y:
        x *= i
    return x

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')



def fact(n):
    if n==1:
        return 1
    else:
        tmp = n * fact(n-1)
        #print(tmp)
        return tmp



def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num -1,num*product)
