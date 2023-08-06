

def trim(v):
    if len(v) <= 0:
        return ''
    s = str(v)
    for i in range(1,len(s)):
        if s[i-1:i] == ' ':
            continue
        else:
            s = s[i-1:]
            break
    i = len(s)
    while i > 0:
        if s[i-1:i] == ' ':
            i -= 1
            continue
        else:
            s = s[:i]
            break
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

def trim2(s):
    start = 0
    end = len(s)
    
    # 找到第一个非空格字符的索引
    while start < end and s[start] == ' ':
        start += 1
    
    # 找到最后一个非空格字符的索引
    while start < end and s[end-1] == ' ':
        end -= 1
    
    # 返回去除空格后的字符串
    return s[start:end]

# 测试:
if trim2('hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello') != 'hello':
    print('测试失败!')
elif trim2('  hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim2('') != '':
    print('测试失败!')
elif trim2('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    minValue = L[0]
    maxValue = L[0]
    for v in L:
        if not isinstance(v, (int, float)):
            print('不是数字，无法比较')
            continue
        if v < minValue:
            minValue = v
        if v > maxValue:
            maxValue = v
    print('最小值：%s' % minValue,'最大值：%s' % maxValue)
    return (minValue, maxValue)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


def fib(max):
    n,a,b=0,0,1
    while n <max:
        print(b)
        a,b=b,a+b
        n += 1
    return 'done'


def fib2(max):
    n,a,b=0,0,1
    while n <max:
        yield b
        a,b=b,a+b
        n += 1
    return 'done'

def yh_triangle():
    row = [1]
    while True:
        yield row
        row = [1] + [row[i]+row[i+1] for i in range(len(row) - 1)] + [1]

def yhsj(n):
    g = yh_triangle()
    for i in range(n):
        print(next(g))   
