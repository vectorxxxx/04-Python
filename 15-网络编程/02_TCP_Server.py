import socket
import threading
import time

def test_server():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip和port
    s.bind(('127.0.0.1', 9999))
    # 监听端口
    s.listen(5)
    print('Waiting for connection...')

    # 处理TCP连接
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    test_server()