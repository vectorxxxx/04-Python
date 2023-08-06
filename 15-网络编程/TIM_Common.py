import socket
import threading


class Server(object):
    def __init__(self, nickname, port, ip='localhost'):
        self.nickname = nickname
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def receive(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)
        print('Waiting for connection...')
        sock, addr = self.sock.accept()
        receiveThread = threading.Thread(target=self.__receive_msg, args=(sock, addr))
        receiveThread.start()

    def __receive_msg(self, sock, addr):
        while True:
            data = sock.recv(1024)
            if data.decode('utf-8') == 'bye':
                break
            print('%s' % data.decode('utf-8'))
        sock.close()


class Client(object):
    def __init__(self, nickname, port, ip='localhost'):
        self.nickname = nickname
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def send(self):
        self.sock.connect((self.ip, self.port))
        print('Waiting for connection...')
        sendThread = threading.Thread(target=self.__send_msg)
        sendThread.start()

    def __send_msg(self):
        while True:
            msg = input('Me: ')
            msgStr = ('%s: ' % self.nickname).join(msg)
            print(msgStr)
            self.sock.send(msgStr.encode('utf-8'))


class ServerClient(object):
    def __init__(self, nickname):
        self.nickname = nickname

    def chat(self, portFrom, portTo):
        receiveThread = threading.Thread(target=self.__receive_msg, args=(portFrom,))
        receiveThread.start()
        sendThread = threading.Thread(target=self.__send_msg, args=(portTo,))
        sendThread.start()

    def __receive_msg(self, portFrom):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', portFrom))
        s.listen(5)
        print('Waiting for Receive...')
        sock, addr = s.accept()
        while True:
            data = sock.recv(1024)
            if data.decode('utf-8') == 'bye':
                break
            print('%s' % data.decode('utf-8'))
        sock.close()

    def __send_msg(self, portTo):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', portTo))
        print('Waiting for Sending...')
        while True:
            msg = input('Me: ')
            msgStr = ('%s: ' % self.nickname) + msg
            s.send(msgStr.encode('utf-8'))
