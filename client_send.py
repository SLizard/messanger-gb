from socket import *

# клиент который пишет сообщения

ADDRESS = ('localhost', 7777)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS)

while True:
    msg = input('Введите сообщения: ')
    sock.send(msg.encode("UTF-8"))

