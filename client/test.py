from socket import AF_INET,socket,SOCK_STREAM
from threading import Thread
import time

HOST = "localhost"
PORT = 5500
ADDR = (HOST,PORT)
BUFSIZ = 512

messages = []
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messages():
    while True:    
        try:    
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]",e)
            break


def send_message(msg):  
    client_socket.send(bytes(msg,"utf8"))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("Adnan")
time.sleep(10)
send_message("merhaba")
time.sleep(2)
send_message("{quit}")