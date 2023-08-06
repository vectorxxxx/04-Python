import socket


def test_server():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定ip和port
    s.bind(('127.0.0.1', 9999))
    print('Bind UDP on 9999...')
    # 处理TCP连接
    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s!' % data, addr)

if __name__ == '__main__':
    test_server()