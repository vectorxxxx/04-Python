import socket

# AF_INET: 指定IPv4协议
# SOCK_STREAM: 指定TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    b = s.recv(1024)
    if b:
        buffer.append(b)
    else:
        break
data = b''.join(buffer)
print(data)

# 处理数据
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)

s.close()