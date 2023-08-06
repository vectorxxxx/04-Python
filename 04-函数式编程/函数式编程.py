def normalize(name):
    return list(map(fn, name))

def fn(s):
    return s[0].upper() + s[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = normalize(L1)
print(L2)



from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    x1 = s[:s.find('.')]
    y1 = s[s.find('.')+1:]
    print(x1,y1)
    x2 = reduce(lambda x,y:x*10+y, map(int,x1))
    y2 = reduce(lambda x,y:x*10+y, map(int,y1)) / (10**len(y1))
    print(x2, y2, x2+y2)
    return x2+y2

def str2float2(s):
    ss = s.split('.')
    print(ss,list(map(int,ss)))
    return reduce(lambda x,y:x+y/(10**len(ss[1])), map(int,ss)) 

result = str2float2('123.456')
print('str2float(\'123.456\') =', result)
if abs(result - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# 素数/质数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 回数  
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 200))
print('1~200:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
    
L2 = sorted(L, key=by_name)
print(L2)
