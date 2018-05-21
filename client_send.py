from socket import *

# клиент который пишет сообщения

ADDRESS = ('localhost', 10000)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS)

while True:
    msg = input('Введите сообщения: ')
    sock.send(msg.encode("UTF-8"))

