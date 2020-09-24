import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 7777))
s.listen(1)

print("Servidor de chat\n")
while True:
    print("Esperando conexion de cliente")
    sc, addr = s.accept()
    print("Cliente conectado", addr)
    while True:
        recibido = sc.recv(1024)
        if recibido == "quit":
            break
        print("Recibido: ", recibido)
        sc.send("Hola cliente, soy el servidor".encode('utf-8'))

print("Bye bye")
sc.close
s.close
