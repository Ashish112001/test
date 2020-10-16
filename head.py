import socket
from _thread import *
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '172.30.89.113'
port = 8000
server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")


def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()


b = ["" for i in range(10)]
f = ["" for j in range(10)]
my_clients = []


def threaded_client(conn):
    global msga
    while True:
        msga = conn.recv(8)
        msga = msga.decode("utf-8")
        print(msga)
        if msga == "b1x" and f[1] == "":
            b[1] = "x"
            f[1] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b1o" and f[1] == "":
            b[1] = "o"
            f[1] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b2x" and f[2] == "":
            b[2] = "x"
            f[2] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b2o" and f[2] == "":
            b[2] = "o"
            f[2] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b3x" and f[3] == "":
            b[3] = "x"
            f[3] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b3o" and f[3] == "":
            b[3] = "o"
            f[3] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b4x" and f[4] == "":
            b[4] = "x"
            f[4] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b4o" and f[4] == "":
            b[4] = "o"
            f[4] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b5x" and f[5] == "":
            b[5] = "x"
            f[5] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b5o" and f[5] == "":
            b[5] = "o"
            f[5] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b6x" and f[6] == "":
            b[6] = "x"
            f[6] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b6o" and f[6] == "":
            b[6] = "o"
            f[6] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b7x" and f[7] == "":
            b[7] = "x"
            f[7] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b7o" and f[7] == "":
            b[7] = "o"
            f[7] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b8x" and f[8] == "":
            b[8] = "x"
            f[8] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b8o" and f[8] == "":
            b[8] = "o"
            f[8] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b9x" and f[9] == "":
            b[9] = "x"
            f[9] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "b9o" and f[9] == "":
            b[9] = "o"
            f[9] = "1"
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
        if msga == "re":
            for client in my_clients:
                client.send(bytes(msga, "utf-8"))
            msga = ""
        print(b)



def addclientsthread(sock):
    global my_clients
    conn, addr = sock.accept()
    my_clients += [conn]
    print('Client connected on ' + addr[0])
    start_new_thread(threaded_client, (conn,))


while True:
    addclientsthread(s)