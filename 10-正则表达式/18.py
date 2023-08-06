import re

def is_valid_email(addr):
    re_email = re.compile(r'([a-z\.]+)@(\w+\.\w+)')
    return re_email.match(addr)

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


import re

def name_of_email(email):
    match1 = re.match(r'^<(.+?)>\s*(.+)$', email)
    match2 = re.match(r'^([a-z]+)@([a-z]+)\.([a-z]+)$', email)
    if match1:
        return match1.group(1)
    else:
        return match2.group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
