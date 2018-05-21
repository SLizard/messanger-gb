# Программа клиента
from socket import *
import json


hello_message = {
    "action": "presence"
}


s = socket(AF_INET,SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 7777))  # Соединиться с сервером
hello_message_json = json.dumps(hello_message)
hello_message_b = hello_message_json.encode('utf-8')
tm = s.send(hello_message_b)
answer_message = s.recv(1024)
print(answer_message)
s.close()

