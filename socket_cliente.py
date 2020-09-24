import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("127.0.0.1", 7777))

while True:
    mensaje = str(input(">>")).encode('utf-8')
    socket_cliente.send(mensaje)

    recibido = socket_cliente.recv(1024)
    print("Recibido: ", recibido)

print("Bye bye")
socket_cliente.close()
