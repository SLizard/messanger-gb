# Программа сервера
from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 7777))
s.listen(5)  # Переходит в режим ожидания запросов;

while True:
    client, addr = s.accept() # Принять запрос на соединение
    print("Получен запрос на соединение от %s" % str(addr))
    message_json = client.recv(1024)
    message_json_s = message_json.decode('utf-8')
    print(message_json_s)
#    if message_json
    client.send(b'200')
