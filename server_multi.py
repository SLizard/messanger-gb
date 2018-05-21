import select
from socket import socket, AF_INET, SOCK_STREAM

# создать сокет, повешать на адрес
address = ('', 10000)
s = socket(AF_INET, SOCK_STREAM)
s.bind(address)
s.listen(100)
s.settimeout(0.2)   # Таймаут для операций с сокетом

clients = []


def read_requests(r_clients, all_clients):
    # Чтение запросов из списка клиентов

    responses = {}      # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients):
    # Эхо-ответ сервера клиентам, от которых были запросы

    for sock in w_clients:
        for message in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[message].encode("utf-8").upper()
                sock.send(resp)
            except:                 # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

while True:
    try:
        conn, addr = s.accept()
    except OSError as e:
        pass                     # timeout вышел
    else:
        print("Получен запрос на соединение с %s" % str(addr))
        clients.append(conn)
    finally:
        try:
            who_writes, who_reads, e = select.select(clients, clients, clients, 0)
            reqs = read_requests(who_writes, clients)      # Сохраним запросы клиентов
            write_responses(reqs, who_reads, clients)     # Выполним отправку ответов клиентам
        except Exception as e:
            print("Ожидаем подключения клиентов")
            pass  # Ничего не делать, если какой-то клиент отключился

