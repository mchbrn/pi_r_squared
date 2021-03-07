import socket

def sendRequest(data):
    TCP_IP = '192.168.0.37'
    TCP_PORT = 5005 
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(str(data).encode())
    reply = s.recv(BUFFER_SIZE)
    #if sys.argv[1] == "get":
    #    get = s.recv(BUFFER_SIZE)
    s.close()

    print(reply.decode())

    print(data)
