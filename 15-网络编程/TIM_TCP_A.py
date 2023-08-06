from TIM_Common import ServerClient

if __name__ == '__main__':
    # nickname = input('Please input your nickname: ')
    # s = Server(nickname, 8888)
    # s.receive()
    # c = Client(nickname, 9999)
    # c.send()

    nickname = input('Please input your nickname: ')
    sc = ServerClient(nickname)
    sc.chat(8080, 9090)

