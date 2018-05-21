from socket import *
from select import select
import sys

# клиент который читает сообщения

ADDRESS = ('localhost', 10000)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS)

while True:
    msg = sock.recv(1024)
    print(msg.decode("UTF-8"))
